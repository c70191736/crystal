from django.urls import path
from .import views

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),   
    path('templates/', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('search/', views.search, name='search'),

    path("sign-up/", views.register_request, name="register"),
    path("sign-in/", views.login_request, name="login"),
    path("Sign-out/", views.logout_request, name= "logout"),
]