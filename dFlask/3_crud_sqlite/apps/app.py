
from flask import Flask

from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_wtf.csrf import CSRFProtect

# (3-1) CSRF 생성
csrf = CSRFProtect()

#from apps.crud import views as crud_views

# SQLAlchemy 인스턴스 생성
db = SQLAlchemy()
def create_app():

    # 플라스크 인스턴스 생성
    app = Flask(__name__)

    # 앱에 config (설정)
    app.config.from_mapping(
        SECRET_KEY='aaaaaaaa1234',
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False, # warning 출력
        SQLALCHEMY_ECHO=True, # sql 을 콘솔 로그에 출력
        # (3-2)
        WTF_CSRF_SECRET_KEY="Abcde123456789zxy"
    )

    # (2-3) 앱에 SQLAlchemy와 연계
    db.init_app(app)

    # (2-4) 마이그레이트
    Migrate(app, db)

    # (3-3) csrf 를 앱과 연계
    csrf.init_app(app)

    from apps.crud import views as crud_views
    # apps/crud/views.py 안에 crud 앱으로 등록 (앤드포인트 - crud) 뷰 등록
    app.register_blueprint(crud_views.crud, url_prefix='/crud')

    return app

'''
    CSRF : Cross-Site Request Forgeries
        -  웹 앱의 취약점 중 하나로 공격자가 사용자 브라우저를 통해 의도하지 않은 요청을 서버로 보낼 때
    CSRF에 대한 대책 : 의도한 요청과 의도하지 않은 요청 구별하기 위한 방식

'''