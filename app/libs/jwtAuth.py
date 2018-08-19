import jwt
from flask import request
from flask_httpauth import HTTPBasicAuth
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from app.libs.exceptions import AuthFailed

ISS = 'test JWT'
AUD = 'www.test.com'
SUB = 'jwt@test.com'


class Payload:

    def __init__(self, payload):
        self.iss = payload['iss']
        self.iat = payload['iat']
        self.exp = payload['exp']
        self.aud = payload['aud']
        self.sub = payload['sub']
        self.openid = payload['openid']


def create_jwt_token(openid):
    payload = {
        "iss": ISS,
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400 * 7,
        "aud": AUD,
        "sub": SUB,
        "openid": openid,
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')	
    return token


auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(account, password):
    flag, pl = verify_jwt_token()
    if flag:
        return True
    return False


def verify_jwt_token():
    authorization = request.headers.get('Authorization')
    print('*' * 50)
    print(authorization)
    return True, None
    if not authorization:
        raise AuthFailed(msg='Header failed', error_code=1000)
    try:
        authorization_type, token = authorization.split(' ')
        payload = jwt.decode(token, 'secret', audience=AUD, 
                             algorithms=['HS256'])
    except ExpiredSignatureError:
        raise AuthFailed(msg='Expired token', error_code=1001)
    except InvalidTokenError:
        raise AuthFailed(msg='Invalid token', error_code=1002) 

    if payload:
        pl = Payload(payload)
        return True, pl
    return False, None
