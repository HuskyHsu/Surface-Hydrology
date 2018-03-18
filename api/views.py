import asyncio

from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from database.models import WorkExperience, Papers, Members
from process import LHC


def is_blank(s):
    if s != '':
        return s
    else:
        return None

# 登入
def login(request):

    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/CMS/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/CMS/')
    else:
        return render(request, 'signin.html')

# 登出
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

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

# 實驗室成員
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

# 上傳檔案
def upload_file(request):
    # POST and have file
    if request.method == 'POST' and request.FILES != {}:

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
        print(success)
        return HttpResponseRedirect('/CMS/upload_file')

    else:
        print('QQ')
        return HttpResponseRedirect('/CMS/upload_file')
