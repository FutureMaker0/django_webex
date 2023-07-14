from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.
# user 관련된 기능
# 회원가입, 로그인, 로그아웃

# 뷰는 리퀘스트에 대한 리스폰스를 처리하는 곳이다.

### Registration
class Registration(View):
    def get(self, request):
        # if request.user.is_athenticated:
        #     return redirect('blog:list')
        # 회원가입 페이지 - 정보를 입력할 폼을 보여줘야 함.
        form = RegisterForm()
        # render
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_register.html', context)
        # return render(request, 'blog/post_list.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('blog:list')
        

