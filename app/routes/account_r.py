from flask import Blueprint, request
from app.models.account import Account

account_bp = Blueprint('account', __name__, url_prefix='/accounts')

@account_bp.route('/', methods=['GET'])
def get_accounts():
    Accounts = Account.query.all()
    return {'Accounts': [Account.to_dict() for Account in Accounts]}
