from django.shortcuts import render

# Create your views here.
from Blog.models import Article


def home(request):
    post_list=Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})


def archives(request):
    post_list=Article.objects.all()
    return render(request,'archives.html',{'post_list':post_list})

# def detail(request,date,title):
    # try:
    #     date=Article.objects.get(date)
    #     title=Article.objects.get()
