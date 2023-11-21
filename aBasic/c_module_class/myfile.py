'''
myfile.py
'''

# 1. 모듈전체를 참조할 때는 import
'''import mymodule

print('오늘의 날씨는', mymodule.get_weather())
print('오늘은 ', mymodule.get_date())'''

# 2. 모듈임포트할 때 별칭부여 => 원래 이름 안 먹힘
'''import mymodule as mm
print('오늘의 날씨는', mm.get_weather())
print('오늘은 ', mm.get_date())'''

# 3. 모듈에서 필요한 부분만 임포트하기
'''from c_module_class.mypackage.mymodule import get_weather, get_date
print('오늘의 날씨는', get_weather())
print('오늘은 ', get_date())'''

# 4. [참고] - 권장하지 않음
'''from mymodule import get_weather as gw
print('오늘의 날씨는', gw())'''

# 5. 패키지 / 모듈들 / 함수들 => 패키지명으로
'''import mypackage.mymodule

print('오늘의 날씨는', mypackage.mymodule.get_weather())
print('오늘은 ', mypackage.mymodule.get_date())'''

# 6. 패키지 / 모듈들 / 함수들 => 모듈명만
'''from mypackage import mymodule

print('오늘의 날씨는', mymodule.get_weather())
print('오늘은 ', mymodule.get_date())'''

# 7. 패키지 / 모듈들 / 함수들 => 함수명만
'''from mypackage.mymodule import get_weather, get_date

print('오늘의 날씨는', get_weather())
print('오늘은 ', get_date())'''