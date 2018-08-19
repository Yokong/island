from flask import request

from app.libs.redprint import Redprint
from app.libs.yushuBook import YuShuBook
from app.libs.tools import is_isbn_or_key
from app.forms.book import SearchForm, LikeForm
from app.viewModels.book import BookCollection
from app.libs.jwtAuth import auth
from app.modles.base import db
from app.modles.book import Like
from app.libs.exceptions import Success


api = Redprint('book')


@api.route('/search')
def search():
    form = SearchForm().validate_for_api()
    bookCollection = BookCollection()
    q = form.q.data.strip()
    page = form.page.data
    yushuBook = YuShuBook()
    if is_isbn_or_key(q) == 'isbn':
        yushuBook.search_by_isbn(q)
    else:
        yushuBook.search_by_keyword(q, page)
    bookCollection.fill(yushuBook, q)
    return {
        'error_code': 0,
        'msg': 'success',
        'total': bookCollection.total,
        'books': bookCollection.books
    }
        
        
@api.route('/like', methods=['POST'])
@auth.login_required
def like():
    form = LikeForm().validate_for_api()
    with db.auto_commit():
        like = Like()
        like.islike = True
        like.set_attr(form.data) 
        db.session.add(like)
    return Success(msg='like success')


@api.route('/unlike', methods=['POST'])
@auth.login_required
def unlike():
    form = LikeForm().validate_for_api()
    with db.auto_commit():
        like = Like()
        like.islike = False
        like.set_attr(form.data)
        db.session.add(like)
    return Success(msg='unlike success')
