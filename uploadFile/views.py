from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .process import LHC

from django.db import connection

# Create your views here.
def index(request):
    field = [
        {
            "name": "Capa2",
            "fileName": "Capa2_final_storage_1.dat"
        },
        {
            "name": "Capa3",
            "fileName": "Capa3_final_storage_1.dat"
        },
        {
            "name": "Capa4",
            "fileName": "capa4new_Table1.dat"
        },
    ]

    return render(request, 'index.html', {"field": field})

def post_file(request):
    # POST and have file
    if request.method == 'POST' and request.FILES != {}:

        success = {}
        for file in request.FILES.keys():

            site = LHC.Site().create(file)
            success[file] = site.readFile(request.FILES[file]).insert()

        return JsonResponse({
                'success': success,
                })

    else:
        return JsonResponse({
            'success': False,
            })


