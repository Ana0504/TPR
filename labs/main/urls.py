from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tpr1', views.tpr1_upload, name='tpr1'),
    path('tpr2', views.tpr1_upload_Example, name='tpr2'),
    path('tpr3', views.tpr3, name='tpr3'),
    path('tpr4', views.tpr4, name='tpr4'),
    path('tpr5', views.tpr5, name='tpr5'),
]