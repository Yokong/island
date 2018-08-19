from app.libs.httper import HTTP
from app.libs.jwtAuth import create_jwt_token


class WXAuth:
	
	def __init__(self, appid, secret, code):
		self.appid = appid
		self.secret = secret
		self.code = code
		
	def get_token_openid(self):
		url = f'https://api.weixin.qq.com/sns/jscode2session' + \
		f'?appid={self.appid}&secret={self.secret}&js_code={self.code}' + \
		f'&grant_type=authorization_code'
		data = HTTP.get(url)
		openid = data['openid']
		token = create_jwt_token(openid)
		return token, openid
