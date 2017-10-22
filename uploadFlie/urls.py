from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^file$', views.post_file, name='upload_post_file'),
    url(r'$', views.index, name='upload_index'),
    # url(r'^admin/', admin.site.urls),
]
