import json

from flask import Blueprint, request

from app.libs.redprint import Redprint
from app.modles.base import db
from app.modles.user import User
from app.forms.user import RegisterForm, LoginForm


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
    if form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            return {'code': 200, 'msg': '登录成功'}
        else:
            return {'code': 401, 'msg': '账号/密码错误'}
    return {'code': 401, 'msg': '登录失败', 'data': form.errors}
