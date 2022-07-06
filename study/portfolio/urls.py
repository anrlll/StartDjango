from django.urls import path
from .views import helloworldfunc1

urlpatterns = [

    #プロジェクトのurls.pyファイルからアプリのurlpatternsを
    #呼び出す場合には、プロジェクトのurls.pyファイルに記載した文字列情報は含まれない
    path('helloworldapp/', helloworldfunc1),

]
