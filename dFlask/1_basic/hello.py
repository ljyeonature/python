'''hello.py'''


from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    # 파이썬코드
    return "여기는 헬로우 월드"

@app.route('/hello', methods=['get'])
def hello():
    return "헬로우1"

@app.get("/hello2")
def hello2():
    return "헬로우2"

@app.route('/users/<username>')
def get_user(username):
    return username +"님 입장하였습니다"

# http://127.0.0.1:5000/users/홍길동

@app.route('/board/<int:post_id>')
def get_board(post_id):
    return str(post_id) +"번 글을 확인합니다"

# http://127.0.0.1:5000/board/1004