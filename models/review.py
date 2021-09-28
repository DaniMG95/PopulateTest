from db import db


class ReviewModel(db.Model):
    """
    Data model for item
    """
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(250))

    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item = db.relationship('ItemModel')

    def __init__(self, review, item_id):
        """
        ItemModel class constructor
        """
        self.review = review
        self.item_id = item_id

    def json(self):
        """
        Get object in json format
        """
        return {'review': self.review}

    def save_from_db(self):
        """
        save item from db
        """
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        """
        delete item to db
        """
        db.session.delete(self)
        db.session.commit()