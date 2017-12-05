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


def timeSeries(request, *parameter):

    site = LHC.Site().create(parameter[0])
    item = parameter[1]
    startTime = '{}-{}-{}'.format(parameter[2], parameter[4], parameter[5])
    endTime = '{}-{}-{}'.format(parameter[6], parameter[8], parameter[9])
    check = startTime <= endTime

    return JsonResponse({
        'site': parameter[0],
        'startTime': startTime,
        'endTime': endTime,
        'check': check,
        'data': site.timeSeries(item, startTime, endTime) if check else [],
    })