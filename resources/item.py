from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):
    """
    Endpoint /item/<int:id>
    """

    def get(self, id):
        """
        Get itemModel id
        """
        item = ItemModel.find_by_id(id)
        if item:
            return item.json()
        return {'msg':"Item not exist"}, 401

    def put(self, id):
        """
        update average rating of itemModel id
        """
        item = ItemModel.find_by_id(id)
        if item:
            item.rating = item.average_rating()
            item.save_from_db()
            return item.json()
        return {'msg':"Item not exist"}



    def delete(self, id):
        """
        delete itemModel id
        """
        item = ItemModel.find_by_id(id)
        if item:
            item.delete_to_db()
            return {'msg':"Item deleted"}
        return {'msg':"Item not exist"}

class ItemCreate(Resource):
    """
    Endpoint /item>
    """
    parser_item = reqparse.RequestParser()
    parser_item.add_argument('name', type=str, help='review is name', required= True)

    @classmethod
    def post(cls):
        """
        create itemmodel id
        """
        args = cls.parser_item.parse_args()
        name = args['name']
        if ItemModel.find_by_name(name):
            return {'msg':"item exist"}, 401
        item = ItemModel(name)
        item.save_from_db()
        return item.json()


class ItemList(Resource):
    """
    Endpoint /itemlist/
    """
    def get(self):
        """
        Get all itemModels
        """
        return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}