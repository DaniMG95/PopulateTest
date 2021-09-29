from db import db
import statistics

class ItemModel(db.Model):
    """
    Data model for item
    """
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    rating = db.Column(db.Integer)
    reviews = db.relationship('ReviewModel', lazy="dynamic")

    def __init__(self, name):
        """
        ItemModel class constructor
        """
        self.name = name
        self.rating = 0

    def __repr__(self):
        return '<User %r>' % self.name

    def json(self):
        """
        Get object in json format
        """
        return {'name': self.name, 'rating': self.rating, 'reviews': [review.json() for review in self.reviews.all()]}


    @classmethod
    def find_by_name(cls,name):
        """
        Get item by name
        :param name: item name
        :return: ItemModel
        """
        return cls.query.filter_by(name=name).first()

    def average_rating(self):
        """
        Get average rating item by name
        :param name: item name
        :return: integer
        """
        return statistics.mean(([review.rating for review in self.reviews.all()]))

    def save_from_db(self):
        """
        save item from db
        """
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        """
        save item from db
        """
        db.session.delete(self)
        db.session.commit()