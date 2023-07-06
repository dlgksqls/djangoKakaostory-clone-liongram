from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        context = {
            'form' : form
        }
        return render(request,'account/signup.html',context)
    else:
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('account:signup')


def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'account/login.html',context)
    else:
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request,form.user_cache)
            return redirect('index')
        else:
            return render(request,'account/login.html',{'form':form})        