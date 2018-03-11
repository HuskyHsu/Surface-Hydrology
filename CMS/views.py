from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from database.models import Papers, WorkExperience, Members

# 後台 - 工作經歷
@login_required(login_url='/api/login/')
def work_experience(request):

    work_experience = WorkExperience.objects.all().order_by('-start_year')

    return render(request, 'CMS_work_experience.html', {
        'work_experience': work_experience,
        'which': '工作經歷'
    })

# 後台 - 代表著作
@login_required(login_url='/api/login/')
def papers(request):

    papers = Papers.objects.all().order_by('-date')

    return render(request, 'CMS_papers.html', {
        'papers': papers,
        'which': '代表著作'
    })

# 後台 - 成員管理
@login_required(login_url='/api/login/')
def members(request):

    members = Members.objects.all().order_by('-type', '-pid')

    return render(request, 'CMS_members.html', {
        'members': members,
        'which': '實驗室成員'
    })

# 後台 - 上傳測站資料
@login_required(login_url='/api/login/')
def upload_file(request):

    field = [
        {
            "name": "Capa2",
            "fileName": "Capa2_final_storage_1.dat"
        },
        {
            "name": "Capa3",
            "fileName": "Capa3_final_storage_1.dat"
        },
        {
            "name": "Capa4",
            "fileName": "capa4new_Table1.dat"
        },
    ]

    return render(request, 'CMS_upload_file.html', {
        "field": field,
        'which': '蓮華池測站資料上傳'
    })