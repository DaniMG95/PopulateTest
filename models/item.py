from db import db


class ItemModel(db.Model):
    """
    Data model for item
    """
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    reviews = db.relationship('ReviewModel', lazy="dynamic")

    def __init__(self, name):
        """
        ItemModel class constructor
        """
        self.name = name

    def json(self):
        """
        Get object in json format
        """
        return {'name': self.name, 'items': [review.json() for review in self.reviews.all()]}


    @classmethod
    def find_by_name(cls,name):
        """
        Get item by name
        :param name: item name
        :return: ItemModel
        """
        return cls.query.filter_by(name=name).first()

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