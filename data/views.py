from django.shortcuts import render
from process import LHC

# Create your views here.
def view(request):

    sites = ["Capa2", "Capa3", "Capa4"]

    # siteBasic = []
    siteBasic = [LHC.Site().create(siteName).Basic() for siteName in sites]
    # for siteName in sites:
    #     site = LHC.Site().create(siteName)
    #     siteBasic.append(site.Basic())

    # print(siteBasic)
    return render(request, 'data_view.html', {"siteBasic":siteBasic})