from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from main.models import JobList

# Create your views here.
employments = ['part time jobs', 'full time jobs', 'remote jobs', 'internships', 'contract', 'training']
seniority = ['Student level', 'Entry level', 'mid level', 'Senior level', 'directors', 'VP and above']
salary_ranges = ['$700-$1000', '$1000-$1200', '$1200-$1400', '$1500-$1800', '$2000-$3000']
lst = [i for i in range(100)]


def homePage(request):
    order = request.GET.get('order')
    jobsall = JobList.objects.all().order_by(order)
    item_per_page = 12
    total = jobsall.count()
    page = int(request.GET.get('page'))
    try:
        part_time_jobs = request.POST.get("part time jobs")
        full_time_jobs = request.POST.get("full time jobs")
        remote_jobs = request.POST.get("remote jobs")
        internships = request.POST.get("internships")
        contract = request.POST.get("contract")
        training = request.POST.get("training")
        seniority_level = request.POST.get('seniority-label')
        salary_rangesre = request.POST.get('salary-ranges')
    except:
        pass
    start, end = item_per_page * (page - 1) + 1, item_per_page * page
    end = min(end, total)
    paginator = Paginator(jobsall, item_per_page)
    jobs = paginator.get_page(page)
    context = {'employments': employments,
               'seniority': seniority,
               'salary_ranges': salary_ranges,
               'lst': lst,
               'jobs': jobs,
               'start': start,
               'end': end,
               'total': total
               }

    return render(request, 'main/index.html', context)


def loggedOut(request):
    if (request.user.is_authenticated):
        return redirect('/accounts/logout')
    return render(request, 'account/loggedout.html')
