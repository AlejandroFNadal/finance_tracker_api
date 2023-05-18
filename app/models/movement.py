"""SQLAlchemy class to describe a money operation"""
from app.extensions import db
from app.models.classes import Classes
from app.models.currency import CurrencyVal
from app.models.account import Account

from sqlalchemy.orm import relationship

class Movement(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float)
    date = db.Column(db.Date)

    id_class = db.Column(db.Integer, db.ForeignKey('classes.id'))
    classes = relationship("Classes", back_populates="movements")

    id_currency_val = db.Column(db.Integer, db.ForeignKey('currency_val.id'))
    currency_val = relationship("CurrencyVal", back_populates="movements")
    description = db.Column(db.String(128))

    id_account = db.Column(db.Integer, db.ForeignKey('account.id'))
    account = relationship("Account", back_populates="movements")
    account_after = db.Column(db.Float)

    def __repr__(self):
        return f'<Movement {self.amount} {self.currency_val.currency.ticker}>'
