from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import models
from .models import Emp
from .form import Empform


# Create your views here.
def welcome(request):
    return render(request, 'Welcome.html')


def load_form(request):
    if request.method == "POST":
        form = Empform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/show")
    else:
        form = Empform()
    return render(request, "index.html", {'form': form})


def add(request):
    form = Empform(request.POST)
    form.save()


def show_all(request):
    employee = models.Emp.objects.all()
    return render(request,"show.html",{"employee":employee})


def edit(request, id):
    employee = Emp.objects.get(id=id)
    return render(request, "edit.html", {'employee': employee})


def update(request, id):
    employee = Emp.objects.get(id=id)
    form = Empform(request.POST, instance=employee)
    form.save()
    return HttpResponseRedirect('/show')


def delete(request, id):
    employee = Emp.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect('/show')


def search(request):
    given_name = request.POST['name']
    employee = Emp.objects.filter(ename__icontains=given_name)
    return render(request, "show.html", {'employee': employee})
