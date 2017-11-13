from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def siteStatus(request, site):

    # items = Item.objects.filter(list=list_)
    return JsonResponse({
            'success': site,
            })