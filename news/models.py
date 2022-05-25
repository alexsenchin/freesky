from django.db import models

# Create your models here.

class News(models.Model):
    
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

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

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
