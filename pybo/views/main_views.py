from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pyob():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return 'Index'