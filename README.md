# island

## 接口

```
POST: /api/v1/user/register

参数：json
	{
		"email": "xxx@gmail.com",
		"password": "xxxxxxxx"
	}

Response:
	{
		"code": 200,
		"msg": "注册成功",
		"data": {}
	}
```

```
POST: /api/v1/user/login

参数: json
	{
		"email": "xxx@gmail.com",
		"password": "xxxxxxxx"
	}

Response:
	{
		"code": 200,
		"msg": "登录成功",
	}
```

```
GET: /api/v1/book/search?q=9787501524044

参数:
	?q=9787501524044[&page=5]  []内为可选
	?q=Python[&page=5]

Response:
	{
		books: [],
		"code": 200,
		"msg": "成功",
		"total": xx
	}
```
