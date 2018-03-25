from django.shortcuts import render
from database.models import Papers, WorkExperience, Members, Plans
from django.db.models import Q

# 工作經驗
def professor(request):

    work_experience = WorkExperience.objects.all().order_by('-start_year')
    papers = Papers.objects.all().order_by('-date')

    return render(request, 'professor.html', {
        'work_experience': work_experience,
        'papers': papers
    })

# 實驗室成員
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

# 參與計畫
def plans(request):

    most = Plans.objects.filter(unit='科技部/國科會計畫').order_by('-year', '-start_time')
    wra = Plans.objects.filter(unit='經濟部水利署計畫').order_by('-year', '-start_time')
    cwb = Plans.objects.filter(unit='交通部中央氣象局計畫').order_by('-year', '-start_time')
    aec = Plans.objects.filter(unit='行政院原子能委員會放射性物料管理局計畫').order_by('-year', '-start_time')
    other = Plans.objects.filter(unit='產學合作及其他計畫').order_by('-year', '-start_time')

    return render(request, 'plans.html', {
        'most': most,
        'wra': wra,
        'cwb': cwb,
        'aec': aec,
        'other': other
    })