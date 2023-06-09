from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    article = models.TextField()
    audio = models.FileField(upload_to='blog/audio/', blank=True)
    image = models.ImageField(upload_to='blog/images/', blank=True)
    created = models.DateTimeField(default=timezone.now())
    published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


    def publish(self):
        self.published = timezone.now()
        self.save()

    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk' : self.pk})




    