from django.shortcuts import render
from .models import startups
# Create your views here.

def show(r):
    startup_list=startups.objects.all()
    star_dict={'startup_list':startup_list}


    return render(r,'radico/show.html',context=star_dict)