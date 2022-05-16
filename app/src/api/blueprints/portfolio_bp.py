# create portfolio blueprint
# minimum endpoints:
# Create/Update/Delete/GET
# /buy-stock: adds a new stock to an  portfolio
# /sell-stock: removes a stock from the  portfolio

from http import HTTPStatus
import json
from flask import Blueprint, make_response, request
import app.src.db.portfoliodao as portfoliodao
from app.src.domain.Potfolio import Potfolio

portfolio_bp = Blueprint('portfolio', __name__, url_prefix='/portfolio') 
# url_prefix means that any endpoint declared as part of this blueprint will need to have /investor appended to it

@portfolio_bp.route('/', methods=['GET'])
def default():
    res = make_response()
    res.response=  'OK'
    return res


@portfolio_bp.route('/get-portfolio-by-id/<id>', methods=['GET'])
def get_portfolio_by_id(id):
    try:
        portfolio = portfoliodao.get_portfolio_by_id(id)
        res = make_response()
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        res.response = json.dumps(portfolio.__dict__)
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting investor with id {id}: {str(e)}'
        return error_res

@portfolio_bp.route('/get-portfolios-by-name', methods=['GET'])
def get_portfolios_by_name(): # expects query parameter name, if not available it will get all investors
    try:
        portfolios = []
        name = request.args.get('name')
        portfolios = portfoliodao.get_all_portfolios() if name is None else portfoliodao.get_portfolio_with_name(name)
        res = make_response()
        res.response = json.dumps([portfolio.__dict__ for portfolio in portfolio])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting portfolio with name {name}: {str(e)}'
        return error_res
        
@portfolio_bp.route('/create', methods=['POST'])
def create_portfolio():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type is None or content_type != 'application/json':
            return ('Expected application/json content-type', HTTPStatus.METHOD_NOT_ALLOWED)
        else:
            data = request.json
            portfolio = portfolio.from_dict(data)
            portfoliodao.create_portfolio(portfolio)
            res = make_response()
            res.status = HTTPStatus.OK
            return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while creating a new portfolio: {str(e)}'
        return error_res

@portfolio_bp.route('/update-address/<id>/<new_addr>', methods=['PUT'])
def update_portfolio_status(id, new_addr):
    try:
        portfoliodao.update_portfolio_address(id, new_addr)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while updating investor (ID: {id}) address: {str(e)}'
        return error_res

@portfolio_bp.route('/delete-portfolio/<id>', methods = ['DELETE'])
def delete_portfolio(id):
    try:
        portfoliodao.delete_portfolio_by_id(id)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while deleteing investor (ID: {id}) address: {str(e)}'
        return error_res