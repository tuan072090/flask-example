from werkzeug.wrappers import Request, Response, ResponseStream
from flask import Flask, g
from flask_httpauth import HTTPTokenAuth
auth = HTTPTokenAuth()

tokens = {
    "secret-token-1": "john",
    "secret-token-2": "susan"
}


@auth.verify_token
def verify_token(token):
    print("token....", token)
    if token in tokens:
        g.current_user = tokens[token]
        return True
    return False


class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        # print("chay middleware.......", request.headers.get("Authorization"))

        return self.app(environ, start_response)

