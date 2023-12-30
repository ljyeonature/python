''' apps/crud/models.py'''

from datetime import datetime
from apps.app import db
from werkzeug.security import generate_password_hash

# db.Model 클래스를 상속하여 User 클래스 정의
class User(db.Model):
    # 테이블명 지정
    __tablename__ = "users"

    # 컬럼정의
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String,  index=True)
    email         = db.Column(db.String,  unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at    = db.Column(db.DateTime, default=datetime.now)
    updated_at    = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # 비밀번호 처리
    @property
    def password(self):
        raise AttributeError("읽지못함")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)



'''
데이터베이스 초기화
    flask db init       -> migrations 폴더 생성
        
마이그레이션
    flask db migrate    -> versions 폴더에 파일 (데이터베이스 적용하기 전의 정보)
    
실제 데이터베이스에 반영
    flask db upgrade

'''

    