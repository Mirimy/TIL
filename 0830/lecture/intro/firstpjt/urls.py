"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # include 함수도 가져와서 
# from articles import views
# from pages import views


urlpatterns = [
    path('admin/', admin.site.urls),        # 관리자 페이지

    # # index 페이지
    # path('index/', views.index),
    
    # # greeting 페이지
    # path('greeting/', views.greeting),      # 장고에서는 보통 , 붙이고 끝낸다

    # # diner 페이지
    # path('dinner/', views.dinner),

    # # 사용자가 직접 data를 입력해서 요청 보내는 페이지
    # path('throw/', views.throw),

    # # throw.html 에서 사용자가 입력한 data 받을 곳
    # path('catch/', views.catch),

    # # 사용자의 이름에 따라 다른 url을 만들고 싶을 때 (ex. 인스타 프로필 url은 계정명/)
    # # 사용자에게 url에 name을 입력 받아서 profile에 인자로 넘겨줄거임.
    # # index/ greeting/ dinner/ 등은 사용할 수 없도록 조치해야 함.
    # # 리스트 순서상으로 앞쪽에 있는 요소부터 순회하기 때문에 주의해줘야 한다.
    # # <int:name> 하면 정수만 입력받는다 ( 문자열 입력하면 error )
    # path('<str:name>/', views.profile),

    path('articles/', include('articles.urls')),        # articles 랑 pages 의 path는 각 폴더의 urls 파일에서 따로 관리
    path('pages/', include('pages.urls')),
]
