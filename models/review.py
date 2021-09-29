from db import db


class ReviewModel(db.Model):
    """
    Data model for item
    """
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(250))
    rating = db.Column(db.Integer)

    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item = db.relationship('ItemModel')

    def __init__(self, review, rating, item_id):
        """
        ItemModel class constructor
        """
        self.review = review
        self.item_id = item_id
        self.rating = rating

    def json(self):
        """
        Get object in json format
        """
        return {'review': self.review, 'rating': self.rating,'item_id': self.item_id}

    def save_from_db(self):
        """
        save item from db
        """
        db.session.add(self)
        db.session.commit()
