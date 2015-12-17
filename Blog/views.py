from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from Blog.models import Article, Photo


def home(request):
    posts=Article.objects.all()
    paginator=Paginator(posts,2)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.paginator(paginator.num_pages)
    return render(request,'home.html',{'post_list':post_list})


def archives(request):
    post_list=Article.objects.all()
    return render(request,'archives.html',{'post_list':post_list})

# def detail(request,date,title):
    # try:
    #     date=Article.objects.get(date)
    #     title=Article.objects.get()
def detail(request,year,month,day,title):
    try:
        post = Article.objects.get(date_time__year=year,
                                      date_time__month=month,
                                      date_time__day=day,
                                      title=title)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'post' : post})

def tag(request,tag):
    try:
        post_list=Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'tags.html',{'post_list':post_list})

def photos(request):
    post_list=Photo.objects.all()
    return render(request,'photos.html',{'post_list':post_list});
