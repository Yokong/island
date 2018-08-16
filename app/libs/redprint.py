from flask import Blueprint


class Redprint:
    """红图"""

    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **ops):
        def decorator(f):
            self.mound.append((rule, f, ops))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for rule, f, ops in self.mound:
            endpoint = ops.pop('endpoint', f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **ops)
