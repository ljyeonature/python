import requests

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : 'lbOvUjFPDGFHQpbUWMJeTwzByNcyZTOfZFRdVNhCSX1KHq6h9tZDG82RqEGCPj5lD1VNB%2FKbe5dLoPClziQtXA%3D%3D', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'json', 'base_date' : '20231231', 'base_time' : '0600', 'nx' : '55', 'ny' : '127' }

response = requests.get(url, params=params)
print(response.content)