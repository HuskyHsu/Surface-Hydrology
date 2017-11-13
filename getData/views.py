from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from uploadFile.process import LHC

# Create your views here.
def siteStatus(request, capa):

    site = LHC.Site().create(capa)

    return JsonResponse({
            'success': site.status(),
            'data': site.timeSeries('2015-07-30', '2015-08-17'),
            })