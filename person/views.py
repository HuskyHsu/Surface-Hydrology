from django.shortcuts import render
from database.models import Papers, WorkExperience, Members
from django.db.models import Q

# Create your views here.
def professor(request):

    work_experience = WorkExperience.objects.all().order_by('-start_year')
    papers = Papers.objects.all().order_by('-date')

    return render(request, 'professor.html', {
        'work_experience': work_experience,
        'papers': papers
    })

def members(request):

    masters = Members.objects.filter(Q(type='碩士生') | Q(type='博士生')).order_by('type')
    assistants = Members.objects.filter(type='研究助理')

    graduates = Members.objects.filter(type='畢業生').order_by('master_graduation_year')

    def sort_gra(x):
        return x.master_graduation_year if x.doctor_graduation_year == None else x.doctor_graduation_year
    graduates = sorted(graduates, key = sort_gra)

    return render(request, 'members.html', {
        'masters': masters,
        'assistants': assistants,
        'graduates': graduates
    })
