"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""
from pathlib import Path
import shutil

# shutil.copy('Ex00.txt', Path('imsi/copy_ex.txt'))

# shutil.copytree('imsi', '../copytree')

shutil.rmtree('imsi')