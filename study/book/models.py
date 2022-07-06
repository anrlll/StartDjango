from django.db import models

#migration作成
#python manage.py makemigrations app名

#superuser作成
#python manage.py createsuperuser

class SampleModel(models.Model):
    title = models.CharField(max_length=100)#データ最大長100
    number = models.IntegerField()


CATEGORY = (('business','ビジネス'),('life','生活'),('other','その他'))

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices = CATEGORY


    )

    #class内に記載する
    #データベース　オブジェクト名が変更される
    def __str__(self):
        return self.title

#Djangoで準備されているフィールド
#https://docs.djangoproject.com/ja/3.2/ref/models/fields/

