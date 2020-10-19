from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .forms import Fillup_Form
from main.models import JobList

# Create your views here.
employments = ['part time jobs', 'full time jobs', 'remote jobs', 'internships', 'contract', 'training']
seniority = ['Student level', 'Entry level', 'mid level', 'Senior level', 'directors', 'VP and above']
salary_ranges = ['$700-$1000', '$1000-$1200', '$1200-$1400', '$1500-$1800', '$2000-$3000']
lst = [i for i in range(100)]


def homePage(request):
    order = request.GET.get('order')
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

    jobsall = JobList.objects.all().order_by(order)
    item_per_page = 12
    total = jobsall.count()
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


def redirecthome(request):
    return redirect('/jobs/?page=1&order=-postdate')

class fillupForm(View):
    @method_decorator(login_required)
    def get(self, request,uniq_id):
        form=Fillup_Form()
        context={'form':form}
        return render(request, 'main/fillupform.html', context)

    @method_decorator(login_required)
    def post(self, request,uniq_id):
        form = Fillup_Form(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=request.user
            obj.uniq_id=JobList.objects.filter(id=uniq_id)[0]
            form.save()
        return redirect('/')
        # user = request.user.id
        # firstName = request.POST.get("firstName")
        # lastName = request.POST.get("lastName")
        # email = request.POST.get("email")
        # city = request.POST.get("city")
        # state = request.POST.get("state")
        # pincode = request.POST.get("pincode")
        # Resume = request.FILES.get("resume")
        #
        # print(user,uniq_id,firstName,lastName,email,city,state,pincode,Resume)
        # return render(request,'main/fillupform.html')
