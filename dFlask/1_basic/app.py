''' app.py '''

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    # 파이썬코드
    return "여기는 파이썬 웹"