from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .process import LHC

# Create your views here.
def index(request):
    return render(request, 'index.html')

def post_file(request):
    # POST and have file
    if request.method == 'POST' and request.FILES != {}:

        data = LHC.Capa3(request.FILES['file'])
        print(data)

        return JsonResponse({
                'success': True,
                })

    else:
        return JsonResponse({
            'success': False,
            })


