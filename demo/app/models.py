from django.db import models
from django.contrib.auth.models import User

from . import apps
# Create your models here.


class Step(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='User')
    step_day = models.DateField('date registered', name='Date')
    steps = models.IntegerField(name='Steps')

    def __str__(self):
        return self.User.username + ' steps for ' + self.Date.strftime('%B %d %Y')

    class Meta:
        unique_together = ('User', 'Date',)