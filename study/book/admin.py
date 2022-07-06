from django.contrib import admin

from .models import Book

#modelsのSampleModelをimport
#from .models import SampleModel

#データベーステーブルを管理画面に認識させる
#admin.site.register(SampleModel)
admin.site.register(Book)


