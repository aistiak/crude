from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Person
# Create your views here.


def IndexView(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    li = Person.objects.all()
    context = {
        'person_list': li,
    }
    return render(request, 'list/index.html', context)


def DetailView(request, name):
    person = Person.objects.get(name=name)
    context = {
        'person': person,
    }
    return render(request, 'list/detail.html', context)


def AddPersonView(request):

    return render(request, 'list/add.html')


def AddPersonToDB(request):
    Name = request.GET['name']
    add = request.GET['add']
    cell = request.GET['cell']
    person = Person(name=Name, add=add, cell=cell)
    person.save()
    return HttpResponseRedirect(reverse('list:index'))


def editPersonView(request, name):
    person = Person.objects.get(name=name)
    context = {
        'person':person,
    }
    return render(request, 'list/editPerson.html',context)


def saveEditedPerson(request):
    id   = request.GET['id']
    name = request.GET['name']
    add  = request.GET['add']
    cell = request.GET['cell']

    person = Person.objects.get(id=id)
    person.name = name 
    person.add = add 
    person.cell = cell 
    person.save()

    return HttpResponseRedirect(reverse('list:index'))