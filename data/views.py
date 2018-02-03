from django.shortcuts import render
from process import LHC

# Create your views here.
def view_data(request):

    sites = ["Capa2", "Capa3", "Capa4"]

    siteBasic = []
    for siteName in sites:
        site = LHC.Site().create(siteName)
        siteBasic.append(site.Basic())

    return render(request, 'view_data.html', {"siteBasic":siteBasic})