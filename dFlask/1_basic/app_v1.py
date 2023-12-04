'''app_v1.py'''


from flask import Blueprint

app = Blueprint('v1', __name__, url_prefix='/v1')

@app.route('/users')
def users():
    return '여기는 v1/users 입니다'

@app.route('/board')
def board():
    return '여기는 v1/board 입니다'