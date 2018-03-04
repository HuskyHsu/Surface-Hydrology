from django.shortcuts import render
from django.http import HttpResponseRedirect
from database.models import WorkExperience, Papers, Members

def is_blank(s):
    if s != '':
        return s
    else:
        return None

# 工作經歷
def work_experience(request):

    if request.method == 'POST':

        if request.POST["type"] == 'add':
            WorkExperience.objects.create(
                unit = request.POST["unit"],
                department = is_blank(request.POST["department"]),
                title = request.POST["title"],
                start_year = int(request.POST["start_Year"]),
                end_year = is_blank(request.POST["end_Year"])
            )
        elif request.POST["type"] == 'modify':
            WorkExperience.objects.filter(pid=request.POST["pid"]).update(
                unit = request.POST["unit"],
                department = is_blank(request.POST["department"]),
                title = request.POST["title"],
                start_year = int(request.POST["start_Year"]),
                end_year = is_blank(request.POST["end_Year"])
            )

        elif request.POST["type"] == 'delete':
            WorkExperience.objects.filter(pid=request.POST["pid"]).delete()

    else:
        print('get')

    return HttpResponseRedirect('/CMS/work_experience')

# 代表著作
def papers(request):

    if request.method == 'POST':

        if request.POST["type"] == 'add':
            Papers.objects.create(
                author = request.POST["author"],
                date = request.POST["date"],
                title = request.POST["title"]
            )
        elif request.POST["type"] == 'modify':
            Papers.objects.filter(pid=request.POST["pid"]).update(
                author = request.POST["author"],
                date = request.POST["date"],
                title = request.POST["title"]
            )

        elif request.POST["type"] == 'delete':
            Papers.objects.filter(pid=request.POST["pid"]).delete()

    else:
        print('get')

    return HttpResponseRedirect('/CMS/papers')

def members(request):

    if request.method == 'POST':

        if request.POST["type_crud"] == 'add':
            Members.objects.create(
	            name = request.POST['name'],
	            type = request.POST['type'],
	            master_graduation_year = is_blank(request.POST['master_graduation_year']),
	            master_disseration_title = is_blank(request.POST['master_disseration_title']),
	            master_disseration_url = is_blank(request.POST['master_disseration_url']),
	            doctor_graduation_year = is_blank(request.POST['doctor_graduation_year']),
	            doctor_disseration_title = is_blank(request.POST['doctor_disseration_title']),
	            doctor_disseration_url = is_blank(request.POST['doctor_disseration_url'])
            )
        elif request.POST["type_crud"] == 'modify':
            Members.objects.filter(pid=request.POST["pid"]).update(
	            name = request.POST['name'],
	            type = request.POST['type'],
	            master_graduation_year = is_blank(request.POST['master_graduation_year']),
	            master_disseration_title = is_blank(request.POST['master_disseration_title']),
	            master_disseration_url = is_blank(request.POST['master_disseration_url']),
	            doctor_graduation_year = is_blank(request.POST['doctor_graduation_year']),
	            doctor_disseration_title = is_blank(request.POST['doctor_disseration_title']),
	            doctor_disseration_url = is_blank(request.POST['doctor_disseration_url'])
            )

        elif request.POST["type_crud"] == 'delete':
            Members.objects.filter(pid=request.POST["pid"]).delete()

    else:
        print('get')

    return HttpResponseRedirect('/CMS/members')