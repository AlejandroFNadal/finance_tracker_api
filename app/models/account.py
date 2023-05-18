'''
    SQLAlchemy ORM model for the account table
    It has a name, a description, a balance and a currency
'''
from app.extensions import db
from app.models.currency import Currency

class Account(db.Model):
    __name__ = "account"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    description = db.Column(db.String(128))
    balance = db.Column(db.Float)
    id_currency = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship("Currency", backref="account")

    movements = db.relationship("Movement", back_populates="account")

    def __repr__(self):
        return f'<Account {self.name}>'
    @classmethod 
    def get_all_accounts():
        return Account.query.all()