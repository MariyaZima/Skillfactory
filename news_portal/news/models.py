from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = Post.objects.filter(author=self).aggregate(Sum('rating'))
        comments_rating = Comment.objects.filter(user=self.user).aggregate(Sum('rating'))
        posts_comments_rating = Comment.objects.filter(post__author=self).aggregate(Sum('rating'))

        self.rating = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):

    objects = None
    article = 'AR'
    news = 'NE'

    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    field_choice = models.CharField(max_length=2, choices=POSITIONS, default=news)
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating_art_new = models.IntegerField(default=0)
    many_to_many_relation = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating_art_new += 1
        self.save()

    def dislike(self):
        self.rating_art_new -= 1
        self.save()

    def preview(self):
        return self.content[0:124] + '...'


class PostCategory(models.Model):
    one_to_many_relation = models.ForeignKey(Post, on_delete=models.CASCADE)
    one_to_many_relation1 = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    objects = None
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=1024)
    comment_datetime = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
