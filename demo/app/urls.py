from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id>/',views.app, name='app'),
    path('create/',views.step_create_view, name='step-create')
 
]