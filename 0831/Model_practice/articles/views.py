from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request) :
    # DB의 전체 데이터를 조회
    articles = Article.objects.all()                # READ => 전체 QuerySet
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def new(request) :
    return render(request, 'articles/new.html')

def create(request) :
    # 사용자의 데이터를 new로부터 받아서 DB에 저장
    title = request.GET.get('title')
    content = request.GET.get('content')

    # DB에 저장 ( CREATE )
    # 1
    # article = Article()
    # article.title = title       # 앞에 title은 Article의 인스턴스 속성, 뒤에 title은 위에서 선언해준 변수명
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    # ... 여기서 데이터를 검증한 후에 save 할 수 있기 때문에 2번 방법을 쓰는 게 좋다.
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)


    return render(request, 'articles/create.html')