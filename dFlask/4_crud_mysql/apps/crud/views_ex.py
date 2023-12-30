from flask import Blueprint, render_template

# Blueprint로 앱을 생성
crud = Blueprint("crud", __name__, static_folder='static', template_folder='templates')

# / 엔드포인트로 요청시 index.html출력
@crud.route("/")
def index():
    return render_template("crud/index.html")

'''
    http://127.0.0.1:5000/crud
        --> apps/crud/templates/crud/index.html
'''

from apps.app import db
from apps.crud.models import User

# http://127.0.0.1:5000/crud/sqlSelect
@crud.route('/sqlSelect')
def sqlSelect():
    result = db.session.query(User).all()
    for row in result:
        print(row.username + "/" , row.email)
    return "콘솔에 sql 문장 확인"

@crud.route('/sqlInsert')
def sqlInsert():
    user = User(username="홍길동2", email="hon2@gmail.com", password="1234")
    db.session.add(user)
    db.session.commit()
    return "다시 검색을 하거나 Sqlite brower로 확인"


# http://127.0.0.1:5000/crud/sqlUpdate
@crud.route('/sqlUpdate')
def sqlUpdate():
    user = db.session.query(User).filter_by(id=1).first()
    user.username = "박씨"
    user.email = "park@gmail.com"
    db.session.add(user)
    db.session.commit()
    return "다시 검색을 하거나 Sqlite brower로 확인"


# http://127.0.0.1:5000/crud/sqlDelete
@crud.route('/sqlDelete')
def sqlDelete():
    user = db.session.query(User).filter_by(id=1)
    db.delete(user)
    db.session.commit()
    return "다시 검색을 하거나 Sqlite brower로 확인"