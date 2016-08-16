from django.db import models
from django.utils import timezone
from PIL import Image


class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text1 = models.TextField()
    image1 = models.ImageField(blank=True)
    text2 = models.TextField()
    image2 = models.ImageField(blank=True)
    text3 = models.TextField()
    image3 = models.ImageField(blank=True)
    text4 = models.TextField()
    image4 = models.ImageField(blank=True)
    text5 = models.TextField()
    image5 = models.ImageField(blank=True)


    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Trademark(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    tm1 = models.ImageField(blank=True)
    
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Slide(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slidetext1 = models.TextField()
    slideimage1 = models.ImageField(blank=True)
    

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
