# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.


class Imagen(models.Model):
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=150,blank=True)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5,blank=True)
    imageFile = models.ImageField(upload_to="images",null=True)


class ImageForm(ModelForm):
    class Meta:
        model = Imagen
        fields = ["url", "title", "description", "type", "imageFile"]