from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    # path('create', views.register_request, name='register'),
    path('create', views.create, name='create'),

    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),

]