from django.db import models

# Create your models here.
from django.utils.encoding import smart_str


class Article(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=50,blank=True)#博客标签
    date_time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(blank=True,null=True)
    views_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

#     null：如果为True，空值将会被存储为NULL，默认为False。
#     blank：如果为True，字段允许为空，默认不允许。
#     def get_absolute_url(self):
#         path = reverse('detail', kwargs={'id':self.id})
#         return "http://127.0.0.1:8000%s" % path


    def __str__(self):
        return self.title

    class Meta:
        ordering=['-date_time']

class Photo(models.Model):
    url = models.CharField(max_length=255, default='', null=True, blank=True)
    path = models.ImageField(upload_to='upload/images/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    photo_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title or self.path.name

    def save(self):
        if self.path:
            self.path.name = smart_str(self.path.name)
        self.published = 1
        self.sync_status = 1
        super(Photo, self).save()

    class Meta:
        ordering=['-photo_time']



class Comment(models.Model):
    author = models.CharField(max_length=100)
    author_email = models.CharField(max_length=100)
    author_ip = models.CharField(max_length=100)
    comment_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True)
    hided = models.BooleanField(default=False)
    duoshuo_id = models.CharField(max_length=50, null=True, blank=True)
    duoshuo_user_id = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.article.title


