from django.shortcuts import render
from . models import Step
from django.views.generic import CreateView

# Create your views here.

def index(request):
    test = Step.objects.order_by('-step_day')
    context = {'test':test}
    return render(request,'app/index.html',context)

class StepCreateView(CreateView):
    model = Step
    fields = ['user','steps','step_day']
    template_name='app/create_new_step.html'
    queryset = Step.objects.all()

    def get_form(self, form_class=None):
        from django.forms.widgets import SelectDateWidget
        form = super(StepCreateView, self).get_form(form_class)
        form.fields['step_day'].widget = SelectDateWidget()
        return form