''' app_endpoint.py '''

from flask import Flask

app = Flask(__name__)

@app.route('/test', endpoint='hello_endpoint')
def test():
    return "헬로우 엔드포인트"


'''

    엔드포인트 : URI에 연결된 함수에 이름(별칭)이라고 생각
    url_for()함수를 통해서 엔드포인트명으로 호출
'''