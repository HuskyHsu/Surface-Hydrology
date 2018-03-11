from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^update/work_experience$', views.work_experience, name='update_work_experience'),
    url(r'^update/papers$', views.papers, name='update_papers'),
    url(r'^update/members$', views.members, name='update_members'),
    url(r'^update/obs_datas$', views.upload_file, name='update_obs_data'),
    # url(r'^(Capa\d+)/output/(.*)/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/$', views.outputData, name='some_view'),
    # url(r'^(Capa\d+)/calendarGraph/(.*)/$', views.calendarGraph, name='calendarGraph'),
    # url(r'^(Capa\d+)/(.*)/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/$', views.timeSeries, name='timeSeries'),
]