from django.urls import path
from .views import (
    index_view,
    login_view,
    register_view,
    logout_view,
    report_view,
    mods_view,
    hidde_view,
    unhidde_view,
)

urlpatterns = [
    path('',index_view,name='index'),
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('logout/',logout_view,name='logout'),
    path('report/<int:id>',report_view,name='report'),
    path('moderator/',mods_view,name='reports'),
    path('hidde/<int:id>',hidde_view,name='hidde'),
    path("unhidde/<int:id>",unhidde_view,name='unhidde'),
]