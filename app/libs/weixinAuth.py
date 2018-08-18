from app.libs.httper import HTTP


class WXAuth:
	
	def __init__(self, appid, secret, code, iss, aud, sub):
		self.appid = appid
		self.secret = secret
		self.code = code
		self.iss = iss
		self.aud = aud
		self.sub = sub
		
	def get_token(self):
		url = f'https://api.weixin.qq.com/sns/jscode2session' + \
		f'?appid={self.appid}&secret={self.secret}&js_code={self.code}' + \
		f'&grant_type=authorization_code'
		data = HTTP.get(url)
		token = self._create_token(data['openid'])
		return token
		
	def _create_token(self, openid):
		payload = {
			"iss": self.iss,
			"iat": int(time.time()),
			"exp": int(time.time()) + 86400 * 7,
			"aud": self.aud,
			"sub": self.sub,
			"openid": openid,
    	}
    	token = jwt.encode(payload, 'secret', algorithm='HS256')	
		return token
