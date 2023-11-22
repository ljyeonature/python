from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())
print(Path.home())



# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
p1 = Path('Ex03_createPath.py')
tm = p1.stat().st_ctime
print(tm)

from datetime import datetime
print(datetime.fromtimestamp(tm))

p1.touch()
print(datetime.fromtimestamp(tm))


# --------------------1----------------------------
# 3. 디렉토리 생성
p = Path('imsi2')
p.mkdir(exist_ok=True)

p3 = Path('temp4/abc/test')
p3.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------
# 4. 파일 생성
with open('imsi/1.txt', 'w', encoding='utf-8') as f:
    f.write("짝꿍님 뭐 먹어요?")

p4 = Path('imsi/2.txt')
p4.write_text('그래서 뭐요?', encoding='utf-8')
# p4.rename('imsi/xxxxx.txt')
p4.replace('imsi/xxxxx.txt')


# ------------------------------------------------
#  5. 경로 제거
# p4 = Path('imsi/1.txt')
# p4.unlink()

f = Path('imsi2')
f.rmdir()
# f.rmdir() -> shutil 패키지 이용