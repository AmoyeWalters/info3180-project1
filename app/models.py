<<<<<<< HEAD
# Add any model classes for Flask-SQLAlchemy here
from app import db
from datetime import datetime

class Movie(db.Model):
    __tablename__ = 'movies'
=======
from app import db

class Property(db.Model):
    __tablename__ = 'properties'
>>>>>>> 894dfe9ee2c179ee44904e2f3251831aaf09e947

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
<<<<<<< HEAD
    poster = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
=======
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    property_type = db.Column(db.String(50))
    location = db.Column(db.String(255))
    photo = db.Column(db.String(255))
>>>>>>> 894dfe9ee2c179ee44904e2f3251831aaf09e947
