"""SurfaceHydrology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from home import views as home_views
from person import urls as person_urls
from CMS import urls as CMS_urls

# from uploadFlie import views as upload_views
from uploadFile import urls as uploadFile_urls
from getData import urls as getData_urls
from data import urls as data_urls

from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.home_page, name='home'),
    url(r'^person/', include(person_urls)),
    url(r'^_data/', include(data_urls)),
    url(r'^CMS/', include(CMS_urls)),
    # url(r'^upload$', upload_views.home_page, name='upload'),
    url(r'^upload/', include(uploadFile_urls)),
    url(r'^data/', include(getData_urls)),
]