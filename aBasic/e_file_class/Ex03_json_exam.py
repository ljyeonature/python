'''

Ex02_json_exam.py

data/sample.json 읽어서
과일명 : 총합

'''

f = open('./data/sample.json', 'r', encoding='utf-8')
data = f.read()

import json
items = json.loads(data)
# print(json.dumps(items))
print(json.dumps(items, indent='\t', ensure_ascii=False))


for k,v in items.items():
    # print(k,'>>',v)
    print(k,':',v['price']*v['count'])
    # print(v['price'], ':', v['count'])






f.close()