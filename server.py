from flask import Flask
from flask_restful import Api
from resources.item import Item
import os


def create_app():
    """
    Generates the server application with its respective endpoints.
    :return:
    Flask: server application
    """
    server = Flask(__name__)
    server.secret_key = os.getenv('key')
    api = Api(server)
    api.add_resource(Item, '/item/')
    return server


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)