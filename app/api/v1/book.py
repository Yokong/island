from flask import request

from app.libs.redprint import Redprint
from app.libs.yushuBook import YuShuBook
from app.libs.tools import is_isbn_or_key


api = Redprint('book')


@api.route('/search')
def search():
    args = request.args
    q = args.get('q', '')
    yushuBook = YuShuBook()
    if is_isbn_or_key(q) == 'isbn':
        yushuBook.search_by_isbn(q)
        return yushuBook.first()
    return {'code': 200, 'msg': 'success'}
