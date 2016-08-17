from django.db import models
from django.utils import timezone
from PIL import Image


class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    title1 = models.CharField(max_length=200)
    text1 = models.TextField()
    image1 = models.ImageField(blank=True)
    price1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    text2 = models.TextField()
    image2 = models.ImageField(blank=True)
    price2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)
    text3 = models.TextField()
    image3 = models.ImageField(blank=True)
    price3 = models.CharField(max_length=200)
    title4 = models.CharField(max_length=200)
    text4 = models.TextField()
    image4 = models.ImageField(blank=True)
    price4 = models.CharField(max_length=200)
    title5 = models.CharField(max_length=200)
    text5 = models.TextField()
    image5 = models.ImageField(blank=True)
    price5 = models.CharField(max_length=200)
    title6 = models.CharField(max_length=200)
    text6 = models.TextField()
    image6 = models.ImageField(blank=True)
    price6 = models.CharField(max_length=200)


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
    tm2 = models.ImageField(blank=True)
    tm3 = models.ImageField(blank=True)
    tm4 = models.ImageField(blank=True)
    tm5 = models.ImageField(blank=True)
    tm6 = models.ImageField(blank=True)
    
    
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
    slidetext2 = models.TextField()
    slideimage2 = models.ImageField(blank=True)
    slidetext3 = models.TextField()
    slideimage3 = models.ImageField()
    aboutustext = models.TextField()
    

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
