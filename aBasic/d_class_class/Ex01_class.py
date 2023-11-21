"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""

'''[ 자바인 경우 ]

class Sample {

    String data = "헬로우";
    String name;
    Sample(String name) {
        this.name = name;
    }
}

Sample s = new Sample("홍길동");
'''

class Sample:
    data = "헬로우"
    # 생성자
    def __init__(self, name):
        self.name = name
        print('__init__ 생성자 호출')
    # 소멸자
    def __del__(self):
       print('__del__ 소멸자 호출')

s = Sample("홍길동")
print(s.data)
print(s.name)
del s
print('-'*50)
















"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
 
"""

class Book:
    cnt = 0             # 클래스변수
    def __init__(self, title):
        self.title = title  # 인스턴스변수
        self.cnt += 1

    def output(self):
        print('제목 : ', self.title)
        print('갯수 : ', self.cnt)

    # 클래스 메소드
    @classmethod
    def classoutput(cls):
        cls.cnt += 1
        # print('제목 : ', cls.title)
        print('갯수 : ',  cls.cnt)
        print('갯수 : ',  Book.cnt)

b1 = Book('행복이란')
b2 = Book('먹고살자')

b1.output()
b2.output()
print('-'*40)
b1.classoutput()
b2.classoutput()
print('-'*40)
Book.classoutput()




'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''

class Animal:
    def move(self):
        print('동물은 움직이다')

class Wolf(Animal):
    # 오버라이딩
    def move(self):
        print('늑대는 4발로 달린다')

    # 부모 move 결과 나옴
    '''def run(self):
        print('늑대는 4발로 달린다')'''

class Human(Animal):
    def move(self):
        print('인간은 2발로 걷는다')

class WolfHuman(Human, Wolf):
    def move(self):
        super().move() #  ????????
        print('늑대인간은 2발로 달린다')




wh = WolfHuman()
wh.move()