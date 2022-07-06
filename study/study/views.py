#HttpResponse import
from django.http import HttpResponse

#TemplateView
from django.views.generic import TemplateView

def helloworldfunc(request):
    responseobject = HttpResponse('<h1>hello world</h1>')
    return responseobject

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'

