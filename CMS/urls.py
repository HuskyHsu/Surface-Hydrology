from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^work_experience', views.work_experience, name='work_experience'),
    url(r'^papers', views.papers, name='papers'),
    url(r'^members', views.members, name='members'),
    url(r'^plans', views.plans, name='plans'),
    url(r'^upload_file_ncu', views.upload_file_ncu, name='upload_file_ncu'),
    url(r'^upload_file', views.upload_file, name='upload_file'),
    url(r'^$', views.work_experience, name=''),
]
