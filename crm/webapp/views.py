from django.shortcuts import render

def home(request):
    #return HttpResponse('Hello, ridwaanhall!')
    
    return render(request, 'webapp/index.html')