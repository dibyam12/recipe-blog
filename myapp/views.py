from django.shortcuts import render

# Create your views here.
from  django.http import HttpResponse

def addMenu(req):
    return render(req, 'addMenu.html')

def home(req):
    name = 'Dibyam Raj Ghimire'
    return render(req,"index.html",context={"name":name})
