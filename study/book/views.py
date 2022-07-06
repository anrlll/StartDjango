from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Book

from django.urls import reverse_lazy

#class-based view
class ListBookView(ListView):
    template_name = 'book_list.html'
    model = Book

class DetailBookView(DetailView):
    template_name = 'book_detail.html'
    model = Book

class CreateBookView(CreateView):
    template_name = 'book_create.html'
    model = Book
    fields = ('title','text','category')

    #フォームでデータを送信する際に必要
    success_url = reverse_lazy('list-book')

class DeleteBookView(DeleteView):
    template_name = 'book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('list-book')

class UpdateBookView(UpdateView):
    model = Book
    fields = (['title', 'text', 'category'])
    template_name = 'book_update.html'
    success_url = reverse_lazy('list-book')

#render学習
def index_view(request):
    #print('index_view is called') #ターミナルに表示
    object_list = Book.objects.all()
    return render(request, 'index.html', {'object_list' : object_list})
    #一つ目の引数は request にする 
    #二つ目は、class-based viewのtemplate_nameのようなもの 
    #三つめはmodel = Bookのようなもの

