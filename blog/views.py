from typing import Any, Dict
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views import View 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, HashTag # 같은 경로의 models에서 Post 가져옴.
from .forms import PostForm, CommentForm, HashTagForm
from django.urls import reverse_lazy, reverse

# Create your views here.
# 블로그 안에 있는 views.py를 열었다.
# models - urls - views 순서로 하는 거에서 끝 단계까지 왔다.

'''
웹 요청을 받는다. url + method로 받는다.
요청을 처리하고 디비에서 필요한 값이 있다면 가져온다.
가져온 값을 가공, 정리해서 응답 형태로 만들어준다.
응답을 반환한다.
그 전에 urls에서 맵핑을 해주는게 우선이다.

fbv 함수 기반 뷰 - 얘가 우선 이해가 되어야 클래스 기반이 이해가 된다.
cbv 클래스 기반 뷰
'''


# 클래스로 동일하게 다시한 번 만들어보자.
class Index(View):
    def get(self, request):
        # return HttpResponse('index page GET class')
        
        # 디비에 접근해서 값을 가져와아 한다.
        # 게시판에 글을 보여줘야되기 때문에 디비에서 값 조회
    
        post_objs = Post.objects.all()
        context = {
            "posts": post_objs
            # "posts": None
        }

        # 렌더의 정석적 인자값 3개
        return render(request, 'blog/post_list.html', context)



# django 자체에 클래스 뷰 기능이 강력하고 편리하다.

# 많이 사용.
# model, template_name, context_object_name,
# paginate_by - 페이지를 어떻게 끊어줄 것인지.
# form_class, form_valid(), get_queryset()


# 어떤 함수를 만들 때, get, post 중 뭐가 필요한지를 제일 먼저 고민해야 한다.
# class Write(LoginRequiredMixin,View): # 이미 로그인된 유저만 받아주겠다.
class Write(View): # 이미 로그인된 유저만 받아주겠다.
    def get(self, request):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html', context)
        # 랜더 함수 안에는 html 풀 네임을 써준다.

    # 사용자에게 값을 받아노는 요청이기 때문에 request.POST를 해줘야 한다.
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # 값이 변할 수 있음을 명시
            post.writer = request.user # 인증된 유저의 값을 writer로 받겠다
            post.save() 
            return redirect('blog:list')
        
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html')


class Update(View):
    def get(self, request, pk): # post_id
        post = Post.objects.get(pk = pk)
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, pk):
        post = Post.objects.get(pk = pk)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)

        form.add_error('유효하지 않은 폼.')
        context = {
            'form': form
        }
        return render(request, 'blog/form_error.html', context)


class Delete(View):
    # get은 필요없다. 별도 삭제 페이지가 없기 때문에.
    def post(self, request, pk):
        post = Post.objects.get(pk = pk)
        post.delete()
        return redirect('blog:list')

    # 클래스 자체에 아예 접근하지 못하게 mixin 필요
    # 로그인이 되었을 때만 삭제 버튼이 보이게.


class DetailView(View):
    def get(self, request, pk): # pk: 디비 post_id, 포스트의 아이디값

        # list -> object 상세 페이지 -> 상세  페이지 하나의 내용
        # pk 값을 왔다갔다, 하나의 인자

        # 데이터베이스 방문
        # 해당 글 
        post = Post.objects.get(pk=pk)

        # 댓글
        # all - 테이블 전체
        # get - 값 하나
        # filter - 조건에 맞는 값
        comments = Comment.objects.filter(post=post)

        # HashTag
        hashtags = HashTag.objects.filter(post=post)

        # 댓글 폼
        comment_form = CommentForm()

        # 해시태그 폼 
        hashtag_form = HashTagForm()

        context = {
            'title': 'Blog',
            'post': post,
            'comments': comments,
            'hashtags': hashtags,
            'comment_form': comment_form,
            'hashtag_form': hashtag_form,
        }
    
        return render(request, 'blog/post_detail.html', context)


class commentWrite(View): # 일반 뷰를 상속
    # 어차피 디테일 페이지에 달릴 것이므로 특정 페이지를 요청하는 get은 불필요
    # def get(self, request):
    #     pass

    def post(self, request, pk):
        form = CommentForm(request.POST)
        
        # 해당 아이디에 해당하는 글을 불러옴.
        post = Post.objects.get(pk=pk)
        
        if form.is_valid():
            # 사용자에게 댓글 내용을 받아옴
            content = form.cleaned_data['content']
            
            # 유저 정보 가져오기
            writer = request.user

            # 댓글 객체 생성
            comment = Comment.objects.create(post=post, content=content, writer=writer)
            # comment = Comment(post=post).save() 해도 동일하다.
            # redirect은 단순히 이동만 시켜준다. 주소만 옮겨준다. render랑은 다르다.
            # Detail에서 렌더링 처리를 해주는 과정이 추가로 필요하다.
        
            return redirect('blog:detail', pk=pk)

        # 폼이 유효하지 않은 경우에 대한 예외처리
        # form.add_error('폼이 유효하지 않습니다.')
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'title': 'Blog',
            'post': post,
            'comments': comment,
            'comment_form': form,
        }
        return render(request, 'blog/post_detail.html', context)


class CommentDelete(View):
    def post(self, request, pk): 
        comment = Comment.objects.get(pk=pk)
        post_id = comment.post.id
        comment.delete()

        return redirect('blog:detail', pk=post_id)
    

class HashTagWrite(View):
    def post(self, request, pk):
        form = HashTagForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            writer = request.user
            post = Post.objects.get(pk=pk)
            Hashtag = HashTag.objects.create(post=post, name=name, writer=writer)
            return redirect('blog:detail', pk=pk)
    
        form.add_error(None, 'Invalid form.')
        comment_form = CommentForm()
        context = {
            'title': 'Blog',
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': comment_form,
            'hashtag_form': form,
        }
        return render(request, 'blog/post_detail.html', context)
    

class HashTagDelete(View):
    def post(self, request, pk):
        hashtag = HashTag.objects.get(pk=pk)
        post_id = hashtag.post.id
        hashtag.delete()

        return redirect('blog:detail', pk=post_id)