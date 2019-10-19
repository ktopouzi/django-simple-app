from django import forms
from .models import Step
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class StepCreateFrom(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['User','Date','Steps']
    def __str__(self):
      return self.User