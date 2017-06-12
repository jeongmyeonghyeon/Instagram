from django.db import models
from django.contrib.auth.models import User

"""
member applications생성
    User모델 구현
        username, nickname
이후 해당 User모델을 Post나 Comment에서 author나 user항목으로 참조할 수 있게
"""


class Post(models.Model):
    author = models.ForeignKey(User)
    photo = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(
        User,
        related_name='like_posts'
    )
    tags = models.ManyToManyField('Tag')


class Comment(models.Model):
    # comment_text = models.CharField(max_length=200)
    post = models.ForeignKey(
        'Post'
    )
    author = models.ForeignKey(User)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


# class PostLike(models.Model):
#     like_or_not = models.BooleanField(default=False)
#     posts = models.ForeignKey(
#         'Post'
#     )
#
#     def __str__(self):
#         return self.like_or_not


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
