from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required


# homepage
def home(request):
    #return HttpResponse('Hello, ridwaanhall!')
    
    return render(request, 'webapp/index.html')

# register user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
            
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)


# login a user
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request,username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
                
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context=context)

@login_required(login_url='my-login')
# dashboard
def dashboard(request):
    return render(request, 'webapp/dashboard.html')


# user logout
def logout(request):
    auth.logout(request)
    return redirect('my-login')