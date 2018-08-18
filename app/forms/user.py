from wtforms import Form, StringField, PasswordField
from wtforms.validators import Email, DataRequired, Length, ValidationError

from app.modles.user import User


class RegisterForm(Form):

    email = StringField(
        validators=[DataRequired(message='邮箱不能为空'),
                    Length(8, 32),
                    Email(message='请输入正确的邮箱')]
    )
    password = PasswordField(
        validators=[DataRequired(message='密码不能为空'),
                    Length(6, 32, message='请输入6~32之间的密码')]
    )

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')


class LoginForm(Form):
    code = StringField(
        validators=[DataRequired(message='code 不能为空')]
    )
