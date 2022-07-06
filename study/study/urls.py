"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#study/views.py helloworldfunc import function-based view
from .views import helloworldfunc

#HelloWorldClass import  class-based view
from .views import HelloWorldClass

urlpatterns = [
    #project study
    path('admin/', admin.site.urls),
    path('helloworldurl/', helloworldfunc),
    path('helloworldurl2/', HelloWorldClass.as_view()),

    #ログイン機能の追加　authに用意されている  logoutも同様
    path('accounts/', include('django.contrib.auth.urls')),


    #app portfolio
        #'' path照合部分に何も記載しない場合、
        #ブラウザアクセス時にどんな文字列があっても、条件に合致することを意味する
    path('', include('portfolio.urls')),

    #app book
    path('', include('book.urls')),

]
