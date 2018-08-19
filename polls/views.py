# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Imagen, ImageForm

# Create your views here.
def index(request):
    lista_imagenes = Imagen.objects.all()
    context = {'lista_imagenes': lista_imagenes}
    return render(request, "polls/index.html", context)

def add_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("images:index"))
    else:
        form = ImageForm()

    return render(request, "polls/image_form.html", {"form": form})
