from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from .models import User
from django.http import HttpRequest,HttpResponseRedirect


# Create your views here.

def index_view(request,pk='',*args, **kwargs):
    template_name='feedapp/index.html'

    if request.user.is_authenticated:
        context={
            'username':request.user.username,
        }
    else:
        context={
            'username':'',
        }
    return render(request, template_name)

def register_view(request,*args, **kwargs):
    template_name='feedapp/register.html'
    errors=''

    form=CustomUserCreationForm()

    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            name_user=form['username'].value()
            passwd=form['password1'].value()
            user=authenticate(username=name_user,password=passwd)
        
            login(request,user)
            return redirect(index_view)
            # req=HttpRequest()
            # req.method="GET"
            # req.user=User.objects.filter(username=name_user)

            # return redirect(index_view)
        errors=form.errors
    
    
    context={
        'form':form,
        'errors':errors,
    }

    return render(request,template_name,context)

def logout_view(request):
    logout(request)
    return redirect(index_view)


def login_view(request,*args, **kwargs):
    template_name='feedapp/login.html'
    
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)     
            
            if user is not None:
                login(request,user)
                return redirect(index_view)

    form=LoginForm()
    context={
        'form':form,
        'error':True,
    }
    return render(request, template_name,context)