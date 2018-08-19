from wtforms import Form, StringField
from wtforms.validators import DataRequired 

from app.forms.base import BaseForm


class LoginForm(BaseForm):
    code = StringField(
        validators=[DataRequired(message='code 不能为空')]
    )
