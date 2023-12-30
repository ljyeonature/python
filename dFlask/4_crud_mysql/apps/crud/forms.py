'''
apps/crudforms.py

'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


# FlaskForm를 상속받은 사용자폼 클래스 정의
class UserForm(FlaskForm):
    username = StringField("사용자명",
                           validators=[DataRequired(message="사용자명은 필수입니다"),
                           Length(max=10,message="10자 이내")])
    email = StringField("이메일주소",
                        validators=[DataRequired(message="이메일은 필수입니다")])
    password = PasswordField("비밀번호")
    submit = SubmitField("입력")