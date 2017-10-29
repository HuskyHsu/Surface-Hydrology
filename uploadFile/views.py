from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .process import LHC, connDB

from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'index.html')

def post_file(request):
    # POST and have file
    if request.method == 'POST' and request.FILES != {}:

        site = LHC.Site().create(request.POST['site'])
        success = site.readFile(request.FILES['file']).insert()
        
        return JsonResponse({
                'success': success,
                'data': site.data,
                })

    else:
        return JsonResponse({
            'success': False,
            })


