from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_view, name='index'),

    #URLにbookという文字列が入っていると、views.pyの中でListBookView
    #と定義されたviewを呼び出す
    path('book/',views.ListBookView.as_view(), name = 'list-book'),

    #DetailViewの場合は、どのデータを使うのか明示する必要がある
    #ListViewは個別のデータを指定する必要はない（全てのデータを持ってくるため）
    path('book/<int:pk>/detail/', views.DetailBookView.as_view(), name = 'detail-book'),
    #<int:pk>　pk = primary key 
    # Djangoでは、自動でprimary keyが割り振られる　
    # 確認したい場合は、migrationsへどうぞ

    #CreateViewの場合、modelのどの部分を使用するかをviewで指定する必要がある
    #book/views.pyを参照
    path('book/create/', views.CreateBookView.as_view(), name = 'create-book'),

    path('book/<int:pk>/delete/', views.DeleteBookView.as_view() ,name='delete-book'),

    path('book/<int:pk>/update/', views.UpdateBookView.as_view() ,name='update-book'),
]
