from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request, 'pages/index.html')

    # 그냥 index.html 이라고 쓰면 INSTALLED APPS 에서 선언된 app들 순차적으로 순회하여
    # 순서상 앞에 있는 app 의 templates 폴더에 있는 index가 나오기 때문에,
    # 이런 문제를 방지하기 위해서 templates 폴더 안에 app 이름 폴더를 만들어서 그 안에 html 파일들을 넣는다.
    # 그리고 앞에 pages/ 나 articles/ 를 추가해주면 해당 app의 같은 html 이름으로 이동하여 중복을 피할 수 있다.
