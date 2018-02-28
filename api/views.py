from django.shortcuts import render
from django.http import HttpResponseRedirect
from database.models import WorkExperience


# Create your views here.
def work_experience(request):

    if request.method == 'POST':

        if request.POST["type"] == 'add':
            WorkExperience.objects.create(
                unit = request.POST["unit"],
                department = request.POST["department"],
                title = request.POST["title"],
                start_year = int(request.POST["start_Year"]),
                end_year = None if request.POST["end_Year"] == "" else int(request.POST["end_Year"])
            )
        elif request.POST["type"] == 'modify':
            
            WorkExperience.objects.filter(pid=request.POST["pid"]).update(
                    unit = request.POST["unit"],
                    department = request.POST["department"],
                    title = request.POST["title"],
                    start_year = int(request.POST["start_Year"]),
                    end_year = None if request.POST["end_Year"] == "" else int(request.POST["end_Year"])
                )

        elif request.POST["type"] == 'delete':
            WorkExperience.objects.filter(pid=request.POST["pid"]).delete()

    else:
        print('get')

    return HttpResponseRedirect('/CMS/work_experience')

