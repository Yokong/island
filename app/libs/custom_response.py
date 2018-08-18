import json
from flask import Response, jsonify


class MyResponse(Response):
    """""自定义返回Response"""

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (list, dict, object)):
            response = json.dumps(response, default=lambda o: o.__dict__)
            response = jsonify(json.loads(response))
        return super(Response, cls).force_type(response, environ)