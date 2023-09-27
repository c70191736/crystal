from django.db import models

from django.contrib.auth.models import User
from django.views.generic import View

from django.conf import settings
from django.conf.urls.static import static

from PIL import Image
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    free = 'free'
    a200 = '200'
    a300 = '300'
    a400 = '400'
    a500 = '500'
    a600 = '600'
    a700 = '700'
    a800 = '800'
    a900 = '900'
    a1000 = '1000'

    amount = [
        (free, 'free'),
        (a200, '200'),
        (a300, '300'),
        (a400, '400'),
        (a500, '500'),
        (a600, '600'),
        (a700, '700'),
        (a800, '800'),
        (a900, '900'),
        (a1000, '1000'),
    ]
    
    title = models.CharField(max_length = 100, default='', blank=True)
    Image = models.ImageField(upload_to='image', default='', blank=True)
    folder = models.FileField(upload_to='folder', default='', blank=True)
    file = models.FileField(upload_to='file', default='', blank=True)
    amount = models.CharField(max_length = 20,choices = amount, default = 'none')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title  

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


        