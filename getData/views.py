from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from uploadFile.process import LHC
import csv

# 取得站資訊
def siteBasic(request, capa):

    if capa != 'all':
        return JsonResponse({
            'success': LHC.Site().create(capa).Basic(),
            })
    else:
        sites = ["Capa2", "Capa3", "Capa4"]
        siteBasic = [LHC.Site().create(siteName).Basic() for siteName in sites]

        return JsonResponse({
            'success': siteBasic,
            })

# 取得時序資料
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

def outputData(request, *parameter):
    # Create the HttpResponse object with the appropriate CSV header.
    site = LHC.Site().create(parameter[0])
    items = parameter[1].split(',')
    startTime = '{}-{}-{}'.format(parameter[2], parameter[4], parameter[5])
    endTime = '{}-{}-{}'.format(parameter[6], parameter[8], parameter[9])
    data = site.outputData(startTime, endTime, items)
    
    filename = "{}-{}-{}-{}.csv".format(parameter[0], ','.join(items), startTime.replace("-", ""), endTime.replace("-", ""))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

    writer = csv.writer(response)

    for row in data:
        writer.writerow(row)

    return response