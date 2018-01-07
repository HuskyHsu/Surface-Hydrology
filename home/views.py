from django.shortcuts import render
from process import LHC

# Create your views here.
def home_page(request):

    sites = ["Capa2", "Capa3", "Capa4"]

    siteBasic = []
    for siteName in sites:
        site = LHC.Site().create(siteName)
        siteBasic.append(site.Basic())

    return render(request, 'home.html', {"siteBasic":siteBasic})