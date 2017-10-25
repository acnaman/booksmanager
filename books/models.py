from django.db import models

# Create your models here.
BUYER_CHOICES = (
    (0, '私物'),
    (1, '会社所有'),
)

DIFFICULTY_CHOICES = (
    (0, ''),
    (1, '初学者向け'),
    (2, '中級者向け'),
    (3, '上級者向け'),
    (4, 'その他'),
)

STARS_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class User(models.Model) :
    id = models.AutoField()
    familyname =  models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)

class Book(models.Model) :
    no = models.AutoField()
    title = models.CharField(max_length=100)
    version = models.CharField(max_length=20, blank=True)
    owner = models.ForeignKey('User')
    buyer = models.IntegerField(default=0, choices=BUYER_CHOICES)
    genre = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    difficulty = models.IntegerField(default=0, choices=DIFFICULTY_CHOICES)
    stars = models.IntegerField(default=3, choices=STARS_CHOICES)
    note = models.CharField(max_length=200, blank=True)
    