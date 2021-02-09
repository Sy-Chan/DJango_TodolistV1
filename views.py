from django.shortcuts import render,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDo_List as td
from .forms import NameForm, CheckForm
from django.db import connection
from . import views

# Create your views here.

def index(request):

    if request.method == 'POST' and "AddItem" in request.POST:
        form1 = NameForm(request.POST)
        T = form1.save()
        return HttpResponseRedirect(reverse('ToDo_List:index'))
    else:
        form1 = NameForm()


    if request.method == 'POST':
        IDs = request.POST.getlist("abc")
        for i in IDs:
            try:
                q = td.objects.get(id=i)
                q.status = True
                now = date.today()
                q.dDate = now
                q.save()
            except ObjectDoesNotExist:
                return HttpResponseRedirect(reverse('ToDo_List:index'))

    if request.method == 'POST' and "delete" in request.POST:
        IDs = request.POST.getlist("abc")
        for i in IDs:
            try:
                q = td.objects.get(id=i)
                q.delete()

            except ObjectDoesNotExist:
                print("can't found it anywhere!")
                return HttpResponseRedirect(reverse('ToDo_List:index'))

    latest_action = td.objects.filter(status= False)
    context = {'latest_action':latest_action,'form1':form1,}

    return render(request, 'ToDo_List/index.html', context)


def history(request):
    latest_action = td.objects.filter(status=True)
    if request.method == 'POST':
        IDs = request.POST.getlist("abc")
        for i in IDs:
            try:
                q = td.objects.get(id=i)
                q.status = False
                q.dDate = None
                q.save()

            except ObjectDoesNotExist:
                print("can't find it anywhere!!")
        return HttpResponseRedirect(reverse('ToDo_List:history'))
    context = {'latest_action':latest_action,}
    return render(request, 'ToDo_List/history.html', context)

def rate(request):
    return HttpResponse('this page is good')
