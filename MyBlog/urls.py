"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','Blog.views.home',name='home'),
    url(r'^archives','Blog.views.archives',name='archives'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<title>\w+)','Blog.views.detail',name='detail'),
    url(r'^tag(?P<tag>\w+)/$','Blog.views.tag',name='tag'),
    url(r'^photos','Blog.views.photos',name='photos'),
    url(r'^upload/images/(?P<path>.*)','django.views.static.serve',{'document_root':'./upload/images'}),

]
