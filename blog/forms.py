# blog/forms.py

from django import forms
from .models import Post, Comment, HashTag


# 일반 Form: html에 있는 form 태그
# 유효성 검사를 위해서 form을 써준다. 
# modelform: model을 사용하는 form
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'head_image', 'file_upload']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'size': '30'})
        }


class HashTagForm(forms.ModelForm):

    class Meta:
        model = HashTag
        fields = ['name']   