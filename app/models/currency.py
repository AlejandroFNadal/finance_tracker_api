'''
    SQLAlchemy model for currency table.
    It has a ticker, a value the conversion rate to
    USD, EUR, Gold and BTC of the currency at that moment
'''
from app.extensions import db

class CurrencyVal(db.Model):
    '''
        Examples could be:
        USD: 1, toEUR: 0.85, toGold: 0.0008, toBTC: 0.0001, Datetime: 2020-05-10 10:00:00
    '''
    __name__ = "currency_val"
    id = db.Column(db.Integer, primary_key = True)
    id_currency = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship("Currency", backref="currencyval")
    usd_value = db.Column(db.Float)
    eur_value = db.Column(db.Float)
    gold_value = db.Column(db.Float)
    btc_value = db.Column(db.Float) 
    wheat_value = db.Column(db.Float)

    movements = db.relationship("Movement", back_populates="currency_val")

class Currency(db.Model):
    '''
        List of currencies
    '''
    __name__ = "currency"
    id = db.Column(db.Integer, primary_key = True)
    ticker = db.Column(db.String(12), index = True, unique = True)