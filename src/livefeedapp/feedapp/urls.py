from django.urls import path
from .views import index_view,login_view,register_view,logout_view

urlpatterns = [
    path('',index_view,name='index'),
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('logout/',logout_view,name='logout'),
]