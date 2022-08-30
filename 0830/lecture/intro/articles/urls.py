from django.urls import path
# 지금 폴더는 articles 폴더니까 굳이 from articles 안해도..?
# 그래도 장고는 정확하게 적어주자. (from . -> 현재폴더에 있는)
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # greeting 페이지
    path('greeting/', views.greeting, name='greeting'),      # 장고에서는 보통 , 붙이고 끝낸다
    # diner 페이지
    path('dinner/', views.dinner, name='dinner'),
    # 사용자가 직접 data를 입력해서 요청 보내는 페이지
    path('throw/', views.throw, name='throw'),
    # throw.html 에서 사용자가 입력한 data 받을 곳
    path('catch/', views.catch, name='catch'),
    # 사용자의 이름에 따라 다른 url을 만들고 싶을 때 (ex. 인스타 프로필 url은 계정명/)
    # 사용자에게 url에 name을 입력 받아서 profile에 인자로 넘겨줄거임.
    # index/ greeting/ dinner/ 등은 사용할 수 없도록 조치해야 함.
    # 리스트 순서상으로 앞쪽에 있는 요소부터 순회하기 때문에 주의해줘야 한다.
    # <int:name> 하면 정수만 입력받는다 ( 문자열 입력하면 error )
    path('<str:name>/', views.profile, name='profile'),
]

# name=' ' 을 선언하면 절대/상대 경로 대신 {% url '이름' %} 으로 불러올 수도 있따.
