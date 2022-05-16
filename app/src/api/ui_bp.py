import imp
from flask import Blueprint

ui_bp = Blueprint('ui', __name__, url_pref)

@ui_bp.route('/')
def home():
    return render_template('home.html')

@ui_bp.route('/about')
def about():
    return render_template('about.html')

@ui_bp.route('/investors')
def investors():
    return render_template('investors.html')