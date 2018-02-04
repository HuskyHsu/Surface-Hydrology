from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^professor', views.professor, name='professor'),
    url(r'^members', views.members, name='members'),
]
