from flask import request
from wtforms import Form

from app.libs.exceptions import ParameterError


class BaseForm(Form):

    def __init__(self):
        data = request.json
        args = request.args.to_dict()
        super().__init__(data=data, **args)

    def validate_for_api(self):
        valid = super().validate()
        if not valid:
            raise ParameterError(msg='parameter error')
        return self
