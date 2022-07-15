import requests

url = 'https://api.agify.io?name=michael'
response = requests.get(url).json()
#url에다가 요청을 보내서 변수에 담을거야(json형식으로)
print(type(response))
name = response['name']
age = response['age']
count = response['count']

print(response['name'])

print('이름이 ' + name + '인 사람의 나이는 ' + str(age) + '입니다.')