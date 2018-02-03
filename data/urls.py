from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view', views.view_data, name='view_data'),
    # url(r'^admin/', admin.site.urls),
]
