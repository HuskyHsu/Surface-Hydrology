from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^(Capa\d+|all)/$', views.siteBasic, name='siteBasic'),
    # url(r'^(Capa\d+)/output/(.*)/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/$', views.outputData, name='some_view'),
    # url(r'^(Capa\d+)/calendarGraph/(.*)/$', views.calendarGraph, name='calendarGraph'),
    # url(r'^(Capa\d+)/(.*)/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/$', views.timeSeries, name='timeSeries'),
]