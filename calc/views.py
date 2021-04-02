from django.shortcuts import render
from django.http import HttpResponse
from calc.models import Internship
# Create your views here.

def home(request):
    dataset = Internship.objects\
        .values('country','year2021','year2020')

    return render(request, "home.html", {'dataset': dataset})

