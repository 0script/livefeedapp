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

    print('start')
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        print('post')
        if form.is_valid():
            form.save()
            print('save')
            messages.success(request,'Account created successfully')
            name_user=form['username'].value()

            req=HttpRequest()
            req.method="GET"
            req.user=User.objects.filter(username=name_user)

            return redirect(index_view)
        errors=form.errors
    

    form=CustomUserCreationForm()

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
    
    print('login')
    if request.method=='POST':
        form=LoginForm(request.POST)
        print('post')
        if form.is_valid():
            print('is valid')
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)     
            print('login')
            print(username)
            print(password)
            if user is not None:
                login(request,user)
                print('uset is not none')
                return redirect(index_view)
                
        
    form=LoginForm()
    print('new form')
    context={
        'form':form,
        'error':True,
    }
    return render(request, template_name,context)
    
    form=LoginForm()
    print(form)
    context={
        'form':form,
        'error':False,
    }
    print('exit render')
    return render(request, template_name,context)
    
    # username=request.POST.get('username')
    # password=request.POST.get('password')
    # user=authenticate(request,username=username,password=password)
    # print('login')
    # print(username)
    # print(password)
    # if user is not None:
    #     login(request,user)
    #     redirect(index_view)
    # else:
    #     context={
    #         'error':True
    #     }

    # return render(request, template_name,context=context)
