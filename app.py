from flask import Flask
from flask_restful import Resource, Api
from router.target import Target
from model.target_model import db
from flask_migrate import Migrate
from middleware.Authen import Middleware

app = Flask(__name__)
app.config.from_object("config")
api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)
app.wsgi_app = Middleware(app.wsgi_app)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return {"message": "resource is not found"}, 404


api.add_resource(Target, '/targets', '/targets/', '/targets/<int:target_id>')


if __name__ == '__main__':
    app.run(debug=True, port=3000)