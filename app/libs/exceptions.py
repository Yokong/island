from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    """自定义异常"""

    code = 500
    msg = 'sorry, somethin is wrong!'
    error_code = 999

    def __init__(self, msg=None, error_code=None, code=None, headers=None):
        if code:
            self.code = code 
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super().__init__(msg)

    def get_body(self, environ=None):
        body = {
            'msg': self.msg,
            'error_code': self.error_code,
            'request': request.method + ' ' + self.get_url_no_param()
        }
        return json.dumps(body)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    def get_url_no_param(self):
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]


class Success(APIException):
    code = 200
    error_code = 0
    msg = 'success'


class AuthFailed(APIException):
    code = 401
    error_code = 1000
    msg = 'Authorization failed'


class ParameterError(APIException):
    code = 400
    msg = 'parameter error'
    error_code = 1003


class SaveDatabaseError(APIException):
    code = 400
    msg = 'save to database error'
    error_code = 1004
