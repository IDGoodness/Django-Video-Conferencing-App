from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='register.html'), name='register'),
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),    
    path('meeting/',views.videocall, name='meeting'),
    path('logout/',views.logout_view, name='logout'),
    path('join/',views.join_room, name='join_room'),
    # path('',views.index, name='index'),
]
