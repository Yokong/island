import json

from flask import Blueprint, request, current_app

from app.libs.redprint import Redprint
from app.modles.base import db
from app.modles.user import User
from app.forms.user import LoginForm
from app.libs.weixinAuth import WXAuth
from app.libs.exceptions import Success


api = Redprint('user')


@api.route('/login', methods=['POST'])
def login():
    form = LoginForm().validate_for_api()
    appid = current_app.config['APPID']
    secret = current_app.config['WX_SECRET']
    code = form.code.data
    wx_auth = WXAuth(appid, secret, code)
    token, openid = wx_auth.get_token_openid()
    with db.auto_commit():
        user = User()
        user.openid = openid
        db.session.add(user)
    return Success()
