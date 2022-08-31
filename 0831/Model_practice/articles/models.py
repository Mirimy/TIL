from django.db import models

# Create your models here.
class Article(models.Model) :   # Model class 정의 => 테이블의 스키마 정의
    title = models.CharField(max_length=10)    # class 변수(인스턴스)가 하나의 필드, <필드이름 = datatype> => 스키마(뼈대)
    content = models.TextField()

    # CharField(max_length= ) : 길이 제한 있는 문자열 필드, max_length 필수인자
    # TextField() : 길이 제한 없는 문자열 필드 

    # id 컬럼은 테이블 생성 시 장고가 자동으로 생성
    # title - VARCHAR(10)
    # content - TEXT

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # DateTimeField() : 날짜 및 시간을 값으로 사용하는 필드
        # 선택 인자
        # auto_now_add : 최초 생성 일자(현재 날짜/시간으로 자동 초기화) => ex 게시물 등록 시간
        # auto_now : 최종 수정 일자(수정될 때마다 날짜/시간 자동 갱신) => ex 업데이트 시간

    def __str__(self) :
        return self.title       # Article.objects 조회 했을 때 title로 나오게