'''app_blueprint.py

Blueprint

    ` 앱을 분할하여 관리
    ` 하나의 app.pu 안에서 모든 라우터가 등록되는 것은 비효율

'''


from flask import Flask
from app_v1 import app as v1_app
from app_v2 import app as v2_app

app = Flask(__name__)

app.register_blueprint(v1_app)
app.register_blueprint(v2_app)