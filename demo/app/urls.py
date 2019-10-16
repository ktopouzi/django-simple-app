from django.urls import path
from . import views

app_name = "demo"
urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.StepCreateView.as_view(), name='step-create')
    
]