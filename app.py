from flask import Flask
from flask_restful import Api
from flask-resful-scaffolding.resource.foo import Foo
from flask-resful-scaffolding.resource.bar import Bar

app = Flask(__name__)
api = Api(app)


api.add_resource(Foo, '/Foo', '/Foo/<string:id>')
api.add_resource(Bar, '/Bar', '/Bar/<string:id>')