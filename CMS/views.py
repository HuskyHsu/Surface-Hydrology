from django.shortcuts import render
from database.models import Papers, WorkExperience, Members

# Create your views here.
def work_experience(request):

    work_experience = WorkExperience.objects.all().order_by('-start_year')

    return render(request, 'CMS_work_experience.html', {
        'work_experience': work_experience,
        'which': '工作經歷'
    })

def papers(request):

    papers = Papers.objects.all().order_by('-date')

    return render(request, 'CMS_papers.html', {
        'papers': papers,
        'which': '代表著作'
    })

def members(request):

    members = Members.objects.all().order_by('-type', '-pid')

    return render(request, 'CMS_members.html', {
        'members': members,
        'which': '實驗室成員'
    })

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