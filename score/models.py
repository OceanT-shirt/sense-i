from django.db import models

# Create your models here.

class TakePicture(models.Model):
    take_pic = models.ImageField(
        verbose_name = 'take_pic',
        upload_to = 'images/',
    )

class ChoosePicture(models.Model):
    choose_pic = models.ImageField(
        verbose_name = 'choose_pic',
        upload_to = 'images/'
    )

class Result(models.Model):
    picture = models.ImageField(
        verbose_name = 'picture'
    )
    result = models.IntegerField(
        verbose_name = 'result'
    )