from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Step(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step_day = models.DateTimeField('date registered')
    steps = models.IntegerField()

    def __str__(self):
        return self.user.username + ' steps for ' + self.step_day.strftime('%B %d %Y')

    def get_absolute_url(self):
        reverse ('demo:step-create')
