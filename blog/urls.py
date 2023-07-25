from django.urls import path
from . import views
# from blog.views import Index

app_name = 'blog'

urlpatterns = [
    path("", views.Index.as_view(), name='list'),

    # 글 상세조회
    path("detail/<int:pk>/", views.DetailView.as_view(), name='detail'),
    
    # 글 작성
    path("write/", views.Write.as_view(), name='write'), # views에 write 함수.

    # 글 수정
    path("detail/<int:pk>/edit/", views.Update.as_view(), name='edit'),

    # 글 삭제
    path("detail/<int:pk>/delete/", views.Delete.as_view(), name='delete'),

    # 댓글 작성
    path("detail/<int:pk>/comment/write/", views.commentWrite.as_view(), name='cm-write'),

    # 댓글 삭제
    path("detail/<int:pk>/comment/delete/", views.CommentDelete.as_view(), name='cm-delete'),

    # 해시태그 작성
    path("detail/<int:pk>/hashtag/write/", views.HashTagWrite.as_view(), name='ht-write'),

    # 해시태그 삭제
    path("detail/<int:pk>/hashtag/delete", views.HashTagDelete.as_view(), name='ht-delete'),

    # 글 검색
    path("search/<str:q>/", views.PostSearch.as_view(), name='search'),

    # 카테고리 검색
    path("category/<str:slug>/", views.CategorySearch, name='category'),

]

# 여기에 정의하는 애들은 서버주소/blog에 정의가 되는 애들이다.

# 함수기반, 클래스기반 뷰의 표기 바업ㅂ이 다르다.
# 캡슐화, 상속 가능.

