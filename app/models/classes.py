'''SQLAlchemy model for types of expenditures, transfers or incomes'''
from app.extensions import db

class Classes(db.Model):
    '''Examples are "Food", "Transport", "Salary"'''
    __name__ = "Classes"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    description = db.Column(db.String(128))

    movements = db.relationship("Movement", back_populates="classes")
