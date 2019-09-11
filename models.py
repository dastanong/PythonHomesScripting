from extensions import db

class Home(db.Model):
    __tablename__ = "homes"
    id = db.Column(db.Integer, primary_key=True)
    sell_price = db.Column(db.Integer)
    list_price = db.Column(db.Integer)
    living = db.Column(db.Integer)
    rooms = db.Column(db.Integer)
    beds = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    age = db.Column(db.Integer)
    arces = db.Column(db.Float)
    taxes = db.Column(db.Integer)