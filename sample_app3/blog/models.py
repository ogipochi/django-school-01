from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('draft','Draft'),
    ('published','Published'),
    ('limited','Limited')
)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status="published")


class Article(models.Model):
    title = models.CharField(max_length=127)
    tag = models.CharField(max_length=127)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=False,blank=False)
    body = models.TextField()
    top_image = models.ImageField(default=None,null=False,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    objects = models.Manager()     # default
    published = PublishedManager() # custom