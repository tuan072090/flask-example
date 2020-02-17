from werkzeug.wrappers import Request, Response, ResponseStream


class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        print("chay middleware.......", request.headers.get("Authorization"))

        return self.app(environ, start_response)