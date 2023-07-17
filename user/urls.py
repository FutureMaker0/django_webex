from django.urls import path
from . import views

app_name = 'user'

# 여기서는 폼이 아니라 동작할 views.py의 동작할 함수를 받아와야 한다.
urlpatterns = [
    # 회원가입
    path("register/", views.Registration.as_view(), name='register'),

    # 로그인
    path("login/", views.Login.as_view(), name='login'),
]