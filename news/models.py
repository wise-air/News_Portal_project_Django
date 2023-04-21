from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.IntegerField(default=0)

    #решение было подсмотрено из вебинара по разбору. Сам не решил
    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('postRating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commRat = self.authUser.comment_set.aggregate(commentRating=Sum('commentRating'))
        cRat = 0
        cRat += commRat.get('commentRating')

        self.authorRating = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    catName = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    article = 'ART'
    news = 'NEW'

    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новость')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    typeChoice = models.CharField(max_length=3, choices=POSITIONS, default=news)
    pubDate = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory', default="Категория")
    headline = models.CharField(max_length=255)
    text = models.TextField(default="Текст статьи")
    postRating = models.SmallIntegerField(default=0)

    def like(self):
        self.postRating += 1
        self.save()

    def dislike(self):
        self.postRating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:64]}...'

    def __str__(self):
        return f'{self.headline.title()}: {self.text[:64]}...'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    postComm = models.ForeignKey(Post, on_delete=models.CASCADE)
    userComm = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default='Напишите свой комментарий')
    dateOfComment = models.DateTimeField(auto_now_add=True)
    commentRating = models.SmallIntegerField(default=0)

    def like(self):
        self.commentRating += 1
        self.save()

    def dislike(self):
        self.commentRating += 1
        self.save()

    def __str__(self):
        return f'{self.comment.title()} (User:{self.userComm})'