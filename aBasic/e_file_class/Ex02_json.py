'''
Ex02_json.py

data/temp.json 파일을 읽어서 출력

'''
# with open('./data/temp.json', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     print(contents)


f = open('data/temp.json','rt', encoding='utf-8')
data = f.read()
print(data)
print(type(data))

import json
items = json.loads(data)
print(items)
print(type(items))

for v in items.items():
    print(v)


for k,v in items.items():
    print(k,'>>',v)
    print(v['No'], ':', v['Job'])

f.close()















