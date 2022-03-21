from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tpr1', views.tpr1_upload, name='tpr1'),
    path('tpr2', views.tpr1_upload_Example, name='tpr2'),
    path('tpr3', views.tpr3, name='tpr3'),
    path('tpr4', views.tpr4, name='tpr4'),
    path('tpr5', views.tpr6_upload, name='tpr5'),
    path('main_pg', views.main_pg, name='main_ais'),
    path('otzivi_pg', views.otzivi_pg, name='otzivi'),
    path('portfolio_pg', views.portfolio_pg, name='portfolio'),
    path('tarif_mini_pg', views.tarif_mini_pg, name='tarif_mini'),
    path('tarif_elite_pg', views.tarif_elite_pg, name='tarif_el'),
    path('tarif_premium_pg', views.tarif_premium_pg, name='tarif_pr'),
    path('tarifs_pg', views.tarifs_pg, name='tarifs'),

]