from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    #return HttpResponse('Hello, ridwaanhall!')
    
    return render(request, 'webapp/index.html')