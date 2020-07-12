from django.shortcuts import render
from django.http.response import HttpResponse
from .models import News

# Create your views here.


# def index(request):
#     # print(request)
#     news = News.objects.all()
#     res = '<h1>Список новостей</h1>'
#     for item in news:
#         res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
#     return HttpResponse(res)

def index(request):
    news = News.objects.order_by('-created_at')
    context = {'news': news,
               'title': 'Список новостей'
               }
    return render(request, template_name='news/index.html', context=context)
