# Create your models here.
from django.db import models

# Create your models here.
# 데이터베이스가 테이블처럼 형태를 가지고 있다.

# 장고에서는 관계형 데이터베이스를 사용한다
# 테이블이나 엑셀 형태를 가지고 있는 것들.

# 장고 블로그를 만들 때 데이터베이스를 만들어야
# 된다고 하면,
# ORM? 데이터베이스를 구축해야 되는 걸 도와주는 것.
# 각각을 클래스로 만들면 알아서 대응되는 
# 테이블을 만들어준다.
# 1:1 대응하는 테이블을 디비에서 만들어준다.
# 이것을 장고의 Orm 기능이라고 한다.


# 클래스 하나가 테이블 하나를 나타낸다.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=10)
    # 생성된 시간만 저장을 한다.
    # 크리에이티드엣은 수정이 되면 안되는 시간 값.
    created_at = models.DateTimeField(auto_now_add=True)
    # 새로 세이브 될 때마다 그 시간을 저장을 해준다.
    updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    writer = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


# class HashTag(models.Model):
#     post = models.ForeignKey('Post', on_delete=models.CASCADE)
#     writer = models.CharField(max_length=128)
#     name = models.CharField(max_length=10)

#     def __str__(self):
#         return self.name

class HashTag(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    writer = models.CharField(max_length=128)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

