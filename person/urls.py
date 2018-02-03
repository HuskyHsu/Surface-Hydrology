from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^professor', views.professor, name='professor'),
    url(r'^member', views.professor, name='member'),
]
