"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path


# (1) 해당 경로와 하위 목록들 확인
# p = Path('c:\Windows')
p = Path('..')
print(p)
print(p.resolve())
print('-'*40)

child = []
# dir 다
for x in p.iterdir():
    # 파일만
    if x.is_file():
        child.append(x)
    # child.append(x)
child = [x for x in p.iterdir() if x.is_file()]

print(child)
print('-'*40)




