from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view', views.view, name='view'),
    # url(r'^admin/', admin.site.urls),
]
