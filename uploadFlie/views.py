from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def post_file(request):
    print('成功惹!?')
    
    if request.method != 'POST':
        return JsonResponse({
            'success': False,
            })

    return JsonResponse({
            'success': True,
            })
