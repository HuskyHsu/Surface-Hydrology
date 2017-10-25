from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .process import LHC

from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'index.html')

def post_file(request):
    # POST and have file
    if request.method == 'POST' and request.FILES != {}:

        data = LHC.Capa3(request.FILES['file'])
        print(data)

        with connection.cursor() as cursor:
            try:
                cursor.executemany("INSERT INTO RAWDATA_Capa3 (TIMESTAMP, T0, T10, T30, T50, SF10, SF30, SF50, SF70, SF90) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", data)
            finally:
                cursor.close()

        return JsonResponse({
                'success': True,
                'data': data,
                })

    else:
        return JsonResponse({
            'success': False,
            })


