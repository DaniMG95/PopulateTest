from flask_restful import Resource
# from models.review import ReviewModel
from models.item import ItemModel

class Item(Resource):
    """
    Endpoint /item/<string:name>
    """

    def get(self, name):
        """
        Get itemModel name
        """
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'msg':"Item not exist"}, 401


    def post(self, name):
        """
        create itemModel name
        """
        if ItemModel.find_by_name(name):
            return {'msg':"Item exist"}, 401
        item = ItemModel(name)
        item.save_from_db()
        return item.json()

    def put(self, name):
        """
        update average rating of itemModel name
        """
        item = ItemModel.find_by_name(name)
        if item:
            item.rating = item.average_rating()
            item.save_from_db()
            return item.json()
        return {'msg':"Item not exist"}



    def delete(self, name):
        """
        delete itemModel name
        """
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_to_db()
            return {'msg':"Item deleted"}
        return {'msg':"Item not exist"}


class ItemList(Resource):
    """
    Endpoint /itemlist/
    """
    def get(self):
        """
        Get all itemModels
        """
        return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}