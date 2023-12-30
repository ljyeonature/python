from flask import Blueprint, render_template

# Blueprint로 앱을 생성
crud = Blueprint("crud", __name__, static_folder='static', template_folder='templates')

# / 엔드포인트로 요청시 index.html출력
@crud.route("/")
def index():
    return render_template("crud/index.html")

# --------------------------------------------------------------------------------

from flask import redirect, url_for
from apps.crud.forms import UserForm
from apps.app import db
from apps.crud.models import User

@crud.route("/users/new", methods=["get","post"])
def create_user():
    # UserForm 인스턴스
    form = UserForm()
    # 폼의 submit 이라면
    if form.validate_on_submit():
        # User 객체를 만들어서 db 입력
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))

    return render_template("crud/create.html", form=form)

# http://127.0.0.1:5000/crud/users
@crud.route("/users")
def users():
    users = User.query.all()
    return render_template("crud/select.html", users=users)


@crud.route("/users/<user_id>", methods=["get", "post"])
def edit_user(user_id):
    form = UserForm()

    # db로부터 User 객체 얻어오기
    user = User.query.filter_by(id=user_id).first()

    # submit() 여부
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))

    return render_template("crud/edit.html", user=user, form=form)

@crud.route("/uers/<user_id>/delete", methods=["post"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))