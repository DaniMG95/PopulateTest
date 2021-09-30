from flask import Flask
from flask_restful import Api
from resources.item import Item, ItemList, ItemCreate
from resources.review import Review
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getenv('path')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('KEY')
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Item, '/item/<int:id>')
api.add_resource(ItemCreate, '/item')
api.add_resource(ItemList, '/items')
api.add_resource(Review, '/review/<int:item_id>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)