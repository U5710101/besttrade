# create account blueprint
# minimum endpoints:
# Create/Update/Delete/GET

from http import HTTPStatus
import json
from flask import Blueprint, make_response, request
import app.src.db.accountdao as accountdao
from app.src.domain.Account import Account

account_bp = Blueprint('account', __name__, url_prefix='/account') 
# url_prefix means that any endpoint declared as part of this blueprint will need to have /account appended to it

@account_bp.route('/', methods=['GET'])
def default():
    res = make_response()
    res.response=  'OK'
    return res

@account_bp.route('/get-all', methods=['GET'])
def get_all():
    try:
        accounts = accountdao.get_all_accounts()
        res = make_response()
        res.response = json.dumps([account.__dict__ for account in accounts])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting all accounts: {str(e)}'
        return error_res

@accounts_bp.route('/get-account-by-id/<id>', methods=['GET'])
def get_account_by_id(id):
    try:
        account = accountdao.get_account_by_id(id)
        res = make_response()
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        res.response = json.dumps(account.__dict__)
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting account with id {id}: {str(e)}'
        return error_res

@account_bp.route('/get-accounts-by-name', methods=['GET'])
def get_accounts_by_name(): # expects query parameter name, if not available it will get all accounts
    try:
        accounts = []
        name = request.args.get('name')
        accounts = accountdao.get_all_accounts() if name is None else accountdao.get_account_with_name(name)
        res = make_response()
        res.response = json.dumps([account.__dict__ for account in accounts])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting account with name {name}: {str(e)}'
        return error_res
        
@account_bp.route('/create', methods=['POST'])
def create_account():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type is None or content_type != 'application/json':
            return ('Expected application/json content-type', HTTPStatus.METHOD_NOT_ALLOWED)
        else:
            data = request.json
            account = Account.from_dict(data)
            accountdao.create_account(account)
            res = make_response()
            res.status = HTTPStatus.OK
            return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while creating a new account: {str(e)}'
        return error_res

@account_bp.route('/update-address/<id>/<new_addr>', methods=['PUT'])
def update_account_status(id, new_addr):
    try:
        accountdao.update_account_address(id, new_addr)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while updating account (ID: {id}) address: {str(e)}'
        return error_res

@account_bp.route('/delete-account/<id>', methods = ['DELETE'])
def delete_account(id):
    try:
        accountdao.delete_account_by_id(id)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while deleteing account (ID: {id}) address: {str(e)}'
        return error_res