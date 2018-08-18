import json

from flask import Blueprint, request, current_app

from app.libs.redprint import Redprint
from app.modles.base import db
from app.modles.user import User
from app.forms.user import RegisterForm, LoginForm
from app.libs.weixinAuth import WXAuth


api = Redprint('user')


@api.route('/register', methods=['POST'])
def register():
    data = request.json
    form = RegisterForm(data=data)
    if form.validate():
        with db.auto_commit():
            user = User()
            user.set_attr(form.data)
            db.session.add(user)
            return {'code': 201, 'msg': '注册成功'}
    return {'code': 400,
            'msg': '注册失败',
            'data': form.errors}


@api.route('/login', methods=['POST'])
def login():
    data = request.json
    form = LoginForm(data=data)
    appid = current_app.config['APPID']
    secret = current_app.config['WX_SECRET']
    if form.validate():
        code = form.code.data
        auth = WXAuth(appid, secret, code)
        token = auth.get_token() 
        return token
