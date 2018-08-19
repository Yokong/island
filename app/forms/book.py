from wtforms import Form, StringField, IntegerField
from wtforms.validators import (Length, NumberRange, DataRequired,
								ValidationError)

from app.modles.user import User
from app.forms.base import BaseForm


class SearchForm(BaseForm):
	q = StringField(
		validators=[Length(min=1, max=30), DataRequired()]
	)
	page = IntegerField(
		validators=[NumberRange(min=1, max=99)],
		default=1
	)
	
	
class LikeForm(BaseForm):
	openid = StringField(
		validators=[DataRequired(message='openid 不能为空')]
	)
	isbn = StringField(
		validators=[DataRequired(message='isbn 不能为空')]
	)
