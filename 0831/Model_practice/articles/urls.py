from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),            # 이거 'index/'로 하면 왜 안됨???
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
