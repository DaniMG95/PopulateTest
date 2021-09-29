from flask_restful import Resource,reqparse
from models.review import ReviewModel

class Review(Resource):
    """
    Endpoint /item/<string:name>
    """

    parser_review = reqparse.RequestParser()
    parser_review.add_argument('review', type=str, help='review is necesary', required= True)
    parser_review.add_argument('rating', type=int, help='rating is necesary', required= True)

    @classmethod
    def post(cls,item_id):
        """
        create ReviewModel
        """
        data = cls.parser_review.parse_args()
        item = ReviewModel(data['review'],data['rating'], item_id)
        item.save_from_db()
        return item.json()

