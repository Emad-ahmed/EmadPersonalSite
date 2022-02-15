from email.mime import image
from pyexpat import model
from django.db import models
from django.utils.timezone import datetime
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    post_data = models.TextField()
    blog_image = models.ImageField(upload_to='images/')
    post_date = models.DateTimeField(default=datetime.now())
