from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from process import LHC

from django.db import connection

import asyncio
from aiomysql import create_pool
import time

now = lambda: time.time()

# 上傳畫面
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

    return render(request, 'uploadFile.html', {"field": field})

# POST位置
def post_file(request):
    # POST and have file
    if request.method == 'POST' and request.FILES != {}:

        start = now()

        # OPEN async
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        # loop = asyncio.get_event_loop()

        # create coroutine object
        tasks = [ asyncio.ensure_future(
            LHC.Site().create(file)
                .readFile( request.FILES[file], request.POST["date"] )
                .asyncInsert(loop)
            ) for file in request.FILES.keys()]

        # run async
        loop.run_until_complete(asyncio.wait(tasks))

        # get return value
        success = [task.result() for task in tasks]

        print('TIME: ', now() - start)
        return render(request, 'checkPage.html', {"success": success, "date": request.POST["date"] })
        # return JsonResponse({
        #         'success': success,
        #         })

    else:
        return render(request, 'checkPage.html', {'success': []})
