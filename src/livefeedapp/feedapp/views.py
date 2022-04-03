from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserCreationForm,LoginForm,PostForm,PostMsgForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required,login_required
from .models import User,Post
from django.http import HttpRequest,HttpResponse
from django.utils import timezone
import datetime

# Create your views here.

def index_view(request,pk='',*args, **kwargs):
    template_name='feedapp/index.html'
    is_mod=False

    if request.user.is_authenticated:
        current_user=get_object_or_404(User,id=request.user.id)
        if is_moderator(request.user):
            is_mod=True
        user={
            'username':request.user.username,
            'id':request.user.id,
            'ismod':is_mod,
        }
    else:
        user={
            'username':'',
            'id':22,
            'ismod':False,

        }

    form=PostMsgForm(request.POST or None)
    posts=Post.objects.filter(hidden=False).order_by('-date_posted').all()
    
    if form.is_valid():
        Post.objects.create(text=form.cleaned_data['text'],user=User.objects.get(id=user['id']))
    else:
        form=PostMsgForm()

    context={
        'username':user['username'],
        'form':form,
        'ismod':user['ismod'],
        'posts':posts,
    }
    return render(request, template_name,context)

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
    
    form=LoginForm(request.POST or None)
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

def is_moderator(user):
    return user.groups.filter(name='Moderators').exists()

def report_view(request,id):
    if request.method=='GET':
        post=get_object_or_404(Post,id=id)
        post.reported=True
        post.save(update_fields=['reported'])
        return HttpResponse('Success!')
    else:
        return HttpResponse('Request method is not GET')


@login_required
def mods_view(request):

    template_name='feedapp/mods.html'
    
    if request.user.is_authenticated and  is_moderator(request.user) :
        user={
            'username':request.user.username,
            'id':request.user.id,
            'ismod':True,
        }
        
        posts=Post.objects.filter( Q(reported=True) | Q(hidden=True) )
        context={
            'username':user['username'],
            'ismod':user['ismod'],
            'posts':posts,

        }
        
        return render(request, template_name,context=context)
    else:
        return redirect(index_view) 

@login_required
def hidde_view(request,id):
    if request.method=='GET' and is_moderator(request.user) :
        post=get_object_or_404(Post,id=id)
        post.hidden=True
        post.save(update_fields=['hidden'])
        post.date_hiden=datetime.datetime.now(tz=timezone.utc)
        post.save(update_fields=['date_hiden'])

        return HttpResponse('Success!')
    else:
        return HttpResponse('Not Authorized')

@login_required
def unhidde_view(request,id):
    if request.method=='GET' and is_moderator(request.user) :
        post=get_object_or_404(Post,id=id)
        post.hidden=False
        post.save(update_fields=['hidden'])
        post.reported=False
        post.save(update_fields=['reported'])

        return HttpResponse('Success!')
    else:
        return HttpResponse('Not Authorized')
