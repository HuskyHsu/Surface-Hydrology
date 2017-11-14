from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .process import LHC

from django.db import connection

import asyncio
import time

now = lambda: time.time()

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

        async def test01(file, FILES, date):
            site = LHC.Site().create(file)
            site.readFile(FILES, date)
            return await site.insert()

        start = now()
        success = []
        tasks = []

        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        for file in request.FILES.keys():

            # coroutine = test01(file, request.FILES[file], request.POST["date"])
            # tasks.append( asyncio.ensure_future(coroutine) )
            site = LHC.Site().create(file)
            site.readFile(request.FILES[file], request.POST["date"])
            success.append({ "name": file, "result": site.insert()})
        
        # loop.run_until_complete(asyncio.wait(tasks))

        # for task in tasks:
        #     print('Task ret: ', task.result())

        print('TIME: ', now() - start)
        return render(request, 'checkPage.html', {"success": success, "date": request.POST["date"] })
        # return JsonResponse({
        #         'success': success,
        #         })

    else:
        return render(request, 'checkPage.html', {'success': []})
