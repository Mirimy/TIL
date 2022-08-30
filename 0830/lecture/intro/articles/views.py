from django.shortcuts import render
import random

# Create your views here.
def index(request) :
    # template 을 return
    return render(request, 'articles/index.html')    # render(request, '파일경로')

def greeting(request) :
    # 뭔가 더 넘겨주고 싶으면 render 함수의 3번째 요소에 딕셔너리 추가
    # html에서 넘겨받아 {{ name }}, {{ foods }}와 같이,
    # 넘겨준 딕셔너리의 {{ key값 }} 의 형태로 사용할 수 있다.
    name = 'Alice'
    foods = ['파스타', '짬뽕', '비빔밥']
    context = {
        'name': name,
        'foods': foods
    }
    return render(request, 'articles/greeting.html', context) 

def dinner(request) :
    dinner = ['떡볶이', '라면', '김밥']
    pick = random.choice(dinner)

    wallet = []

    context = {
        'dinner' : dinner,
        'pick' : pick,
        'wallet' : wallet
    }
    return render(request, 'articles/dinner.html', context)

def throw(request) :
    return render(request, 'articles/throw.html')

def catch(request) :    # throw에서 입력 받아 넘겨준 정보는 request에 담겨있다 !
    print(request.GET)      # 딕셔너리 형태 <QueryDict: {'username': ['장미림']}>
    print(request.GET.get('username'))      # request 에서  value 가져오기 = 장미림
    
    username = request.GET.get('username')
    context = {
        'username' : username
    }
    return render(request, 'articles/catch.html', context)

def profile(request, name) :    # <str:name> 이라는 키워드 인자를 name이라는 변수에 담는다.
    context = {
        'name' : name
    }
    return render(request, 'articles/profile.html', context)