from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from main.models import JobList
from .forms import Fillup_Form

# Create your views here.
employments = ['part time jobs', 'full time jobs', 'remote jobs', 'internships', 'contract', 'training']
no_of_position = ['0-10', '10', '20', '50', '100', '500', '1000']
lst = [i for i in range(100)]


def homePage(request):
    order = request.GET.get('order') if request.GET.get('order') is not None else 'id'
    page = int(request.GET.get('page'))

    jobsall = JobList.objects.all().order_by(order)
    item_per_page = 12
    total = jobsall.count()
    start, end = item_per_page * (page - 1) + 1, item_per_page * page
    end = min(end, total)
    paginator = Paginator(jobsall, item_per_page)
    jobs = paginator.get_page(page)
    context = {'employments': employments,
               'no_of_position': no_of_position,
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


def detailView(request, id):
    job = JobList.objects.filter(id=id)[0]
    return render(request, 'main/detail.html', {'job': job})


class fillupForm(View):
    @method_decorator(login_required)
    def get(self, request, uniq_id):
        form = Fillup_Form()
        job = JobList.objects.filter(id=uniq_id)[0]
        context = {'form': form, 'job': job}
        return render(request, 'main/fillupform.html', context)

    @method_decorator(login_required)
    def post(self, request, uniq_id):
        form = Fillup_Form(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.uniq_id = JobList.objects.filter(id=uniq_id)[0]
            form.save()
        return render(request, 'main/submitted.html', {'uniq_id': uniq_id})
