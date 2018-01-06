from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(Capa\d+|all)/$', views.siteBasic, name='siteBasic'),
    url(r'^(Capa\d+)/(.*)/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])', views.timeSeries, name='timeSeries'),
    url(r'^output/(Capa\d+)/(.*)/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/((19|20)[0-9]{2})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/$', views.outputData, name='some_view'),
    # url(r'^file$', views.post_file, name='upload_post_file'),
    # url(r'$', views.index, name='upload_index'),
    # url(r'^admin/', admin.site.urls),

]