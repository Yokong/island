# island

## 接口


> 登录

```
POST: /api/v1/user/login

参数: json
	{
		'code': 'xxxxx'
	}

Response:
	{
		"error_code": 0,
		"msg": "success",
		"request": "POST xxxxxx"
	}
```

> 搜索

```
GET: /api/v1/book/search?q=9787501524044

参数:
	?q=9787501524044[&page=5]  []内为可选
	?q=Python[&page=5]

Response:
	{
		books: [],
		"error_code": 0,
		"msg": "xxxxx",
		"total": xx
	}
```

> 喜欢
```
POST: /api/v1/book/like
Headers Authorization: JWT xxxxxxxxxxxx

参数:
	{
		"openid": jlkjklj238123123,
		"isbn": 9891231323231231
	}
```
