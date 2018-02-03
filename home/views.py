from django.shortcuts import render
# from process import LHC

# Create your views here.
def home_page(request):

    return render(request, 'home.html')