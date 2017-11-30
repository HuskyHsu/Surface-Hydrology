from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from uploadFile.process import LHC

# Create your views here.
def siteBasic(request, capa):

    if capa != 'all':
        return JsonResponse({
            'success': LHC.Site().create(capa).Basic(),
            # 'data': site.timeSeries('2015-07-30', '2015-08-17'),
            })
    else:
        sites = ["Capa2", "Capa3", "Capa4"]
        siteBasic = [LHC.Site().create(siteName).Basic() for siteName in sites]

        return JsonResponse({
            'success': siteBasic,
            # 'data': site.timeSeries('2015-07-30', '2015-08-17'),
            })


def timeSeries(request, *date):

    startTime = '{}-{}-{}'.format(date[1], date[3], date[4])
    endTime = '{}-{}-{}'.format(date[5], date[7], date[8])
    return JsonResponse({
        'startTime': startTime,
        'endTime': endTime,
        'check': startTime <= endTime
    })