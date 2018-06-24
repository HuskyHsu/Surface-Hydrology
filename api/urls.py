from django.conf.urls import url
from . import views
from . import obs_data

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    
    url(r'^update/work_experience$', views.work_experience, name='update_work_experience'),
    url(r'^update/papers$', views.papers, name='update_papers'),
    url(r'^update/members$', views.members, name='update_members'),
    url(r'^update/plans$', views.plans, name='update_plans'),
    url(r'^update/obs_datas_ncu$', views.upload_file_ncu, name='update_obs_data_ncu'),
    url(r'^update/obs_datas$', views.upload_file, name='update_obs_data'),

    url(r'^get/lhc/(Capa\d+|all)$', obs_data.site_basic, name='get_site_basic'),
    url(r'^get/lhc/(Capa\d+)/output/(.*)/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$', obs_data.output_data, name='get_output_data'),
    url(r'^get/lhc/(Capa\d+)/calendarGraph/(.*)$', obs_data.calendar_graph, name='get_calendar_graph'),
    url(r'^get/lhc/(Capa\d+)/(.*)/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$', obs_data.time_series, name='get_time_series'),
    url(r'^get/lhc/(NCUsite)/(.*)/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$', obs_data.time_series, name='get_time_series'),
]