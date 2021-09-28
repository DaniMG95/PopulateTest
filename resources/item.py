from flask_restful import Resource


class Item(Resource):
    """
    Endpoint /item/
    """
    def get(self):
        return {"hello": "world"}