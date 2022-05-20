# Movie Project



#### 1. 전체 일정



![](readme.assets/전체일정.png)

##### #. Django

- Model

- URL
- View
- Serializer
- DB 저장



##### #. Vue

회원정보

- 회원가입

- 로그인

- 로그아웃

- 프로필

  

각각의 template

- 영화  정보리스트

- 영화 상세 정보

- 시청가능한 플랫폼 확인 (DB에저장)

  



#### 2. 진행상황

##### 5월 20일

> ## Django
>
> >DB, 모델 제작
>
> - 프로젝트 기획 설계
> - 와이어프레임 설계
> - DB 구현 중
>   - TMDB API를 활용하여 데이터를 수집, 가공하여 데이터베이스에 저장 
>   - django 모델 구현
>
> ```python
> from django.db import models
> from django.conf import settings
> from django.core.validators import MaxValueValidator, MinValueValidator
> 
> # Create your models here.
> class Genre(models.Model):
>     name = models.CharField(max_length=50)
> 
> class Cast(models.Model):
>     name = models.CharField(max_length=50)
> 
> class Crew(models.Model):
>     name = models.CharField(max_length=50)
> 
> # class Platform(models.Model):
> #     neflix = models.BooleanField()
> #     watcha = models.BooleanField()
> #     disney = models.BooleanField()
> 
> # class Video(models.Model):
> 
> class Movie(models.Model):
>     genres=models.ManyToManyField(Genre, related_name='movies')
>     casts=models.ManyToManyField(Cast, related_name='movies')
>     crews=models.ManyToManyField(Crew, related_name='movies')
>     title = models.CharField(max_length=100)
>     overview = models.TextField()
>     vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
>     popularity = models.IntegerField()
>     release_date = models.DateTimeField()
>     poster_path = models.TextField()
>     video = models.BooleanField()
> ```
>
> 
>
> 
>
> ## Vue
>
> >뼈대 만드는 작업
>
> ![](readme.assets/메인페이지-16530362615931.png)
>
> 
>
> - 메인페이지 디자인 틀 구상 (TMDB 참고. 추후 변경 할 수 있음)
> - 회원가입, 로그인 , 로그아웃 view, Vuex 제작 ( DB준비되면 테스트 필요 )
>
> ![](readme.assets/컴포넌트구조.png)
>
> 
>
> - 각 컴포넌트 생성





#### 4. 결과





