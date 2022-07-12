from distutils.command.upload import upload
from django.db import models
from embed_video.fields import EmbedVideoField




class News(models.Model):
    
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    video = EmbedVideoField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Projects(models.Model):
    
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Donation(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    collected_amount = models.IntegerField()
    required_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    body = models.TextField()
    
    

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
