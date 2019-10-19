from django.shortcuts import render
from . models import Step
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse
from .forms import StepCreateFrom
from django.utils.dateparse import parse_date
from datetime import datetime
from django.contrib import messages
# Create your views here.
User = get_user_model()


def index(request):
    steps = Step.objects.order_by('-Steps')

    context = {'Steps': steps, "users": User.objects.all()}
    return render(request, 'app/index.html', context)


def step_create_view(request):
    form = StepCreateFrom(request.POST or None)
    if form.is_valid():
        form.save()
        user = form.cleaned_data['User']
        messages.success(request,f'User {user} registerd successfully')
        form = StepCreateFrom()
    else:
        messages.error(request,form.errors)
    context = {
        'form': form
    }

    return render(request,"app/create_new_step.html",context)

# class StepCreateView(CreateView):
#     model = Step
#     fields = '__all__'
#     template_name = 'app/create_new_step.html'
#     queryset = Step.objects.all()

#     def get_success_url(self):
#         return reverse('app:index')

def app(request, id):
    user = User.objects.get(id=id)
    start = request.POST.get('date_start')
    end = request.POST.get('date_end')

    start_date = datetime.strptime(str(start), "%Y-%m-%d").date()
    end_date = datetime.strptime(str(end), "%Y-%m-%d").date()
    steps = user.step_set.filter(
        Date__range=[start_date, end_date]).order_by('Date')
    return render(request, 'partials/_chart.html', {'steps': steps})
