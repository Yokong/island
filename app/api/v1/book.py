from flask import request

from app.libs.redprint import Redprint
from app.libs.yushuBook import YuShuBook
from app.libs.tools import is_isbn_or_key
from app.forms.book import SearchForm, LikeForm
from app.viewModels.book import BookCollection


api = Redprint('book')


@api.route('/search')
def search():
    form = SearchForm(request.args)
    bookCollection = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        yushuBook = YuShuBook()
        if is_isbn_or_key(q) == 'isbn':
            yushuBook.search_by_isbn(q)
        else:
            yushuBook.search_by_keyword(q, page)
        bookCollection.fill(yushuBook, q)
        return {
            'code': 200,
            'msg': 'success',
            'total': bookCollection.total,
            'books': bookCollection.books
        }
        
        
@api.route('/like')
def like():
    form = LikeForm()
    if form.validate():
        pass
            
