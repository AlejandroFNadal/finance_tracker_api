"""SQLAlchemy class to describe a money operation"""
from app.extensions import db
from app.models.classes import Classes
from app.models.currency import CurrencyVal
from sqlalchemy.orm import relationship

class Movement(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float)
    date = db.Column(db.Date)
    id_class = db.Column(db.Integer, db.ForeignKey('classes.id'))
    classes = relationship("Class", back_populates="movements")
    id_currency_val = db.Column(db.Integer, db.ForeignKey('CurrencyVal.id'))
    currency_val = relationship("CurrencyVal", back_populates="movements")
    description = db.Column(db.String(128))
    