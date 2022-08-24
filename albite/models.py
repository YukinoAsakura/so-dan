from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.
class UniversityEmail(models.Model):
    email = models.CharField(max_length=40)

class University(models.Model):
    name = models.CharField(max_length=30)
    email = models.ForeignKey(UniversityEmail, on_delete= models.PROTECT)

class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 245)
#    university = models.ForeignKey(University, on_delete= models.PROTECT)
#    graduate = models.DateField()
    password = models.CharField(max_length=30)


class Experience(models.Model):
    choice =(
            ('FO','飲食'),
            ('AP','アパレル'),
            ('EN','エンジニア'),
            ('SE','接客/サービス'),
            ('OT','その他')
        )
    genre = models.CharField(
        max_length=2,
        choices = choice,
        default = 'FO',
    )
    name = models.CharField(max_length=30)

class Quest(models.Model):
    text = models.TextField()
    published_at = models.DateField(default=timezone.now)
    deadline = models.DateField(blank=True,null=True)
    profile = models.ForeignKey(Profile, on_delete = models.PROTECT)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_at=models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True,null=True)
    like = models.IntegerField(default=0)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
class Chat(models.Model):
    text = models.TextField()
    time = models.DateTimeField(default=timezone.now)
#    profile = models.ForeignKey(Profile, on_delete = models.PROTECT)
    quest = models.ForeignKey(Article,related_name='chats', on_delete = models.PROTECT)

