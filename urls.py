from django.urls import path, reverse
from . import views

app_name='ToDo_List'

urlpatterns = [
path('', views.index, name = 'index'),
path('history', views.history, name='history'),
path('statistics/', views.rate, name='rate')
#first argument is what shown in the urls

]
