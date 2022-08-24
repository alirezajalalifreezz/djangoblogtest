from django.shortcuts import render
from . import models

def home (request):
    articles = models.articles.objects.all().order_by('date')
    args = {'articles': articles}
    return render(request , 'articles/articles_home.html',args)
