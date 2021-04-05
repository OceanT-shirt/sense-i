from django.db import models

# Create your models here.

class Image(models.Model):
   image = models.ImageField(default='default/default.png')

# 撮影した写真を送信する方

class TakePicture(models.Model):
    take_pic = models.ImageField(
        verbose_name = 'take_pic', upload_to = 'images/'
    )

# 選択した写真を送信する方

class ChoosePicture(models.Model):
    choose_pic = models.ImageField(
        verbose_name = 'choose_pic', upload_to = 'media/images/'
    )

class Result(models.Model):
    picture = models.ImageField(
        verbose_name = 'picture'
    )
    result = models.IntegerField(
        verbose_name = 'result'
    )
