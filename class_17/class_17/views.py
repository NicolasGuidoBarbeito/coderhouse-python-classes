from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context


def greeting(request):
    return HttpResponse("Hi Django - Coder")


def introduction(request):
    return HttpResponse("<br><br>We understood this. It's very simple and we can use embedded HTML :)")


def now(request):
    document = f'Now is {datetime.now()}'
    return HttpResponse(document)


def user(request, name: str):
    document = f'My name is {name}'
    return HttpResponse(document)


def year_of_birth(request, age: int):
    current_year = datetime.today().year
    estimated_year_of_birth = current_year - age
    document = f'Your estimated year of birth is {estimated_year_of_birth}'
    return HttpResponse(document)


def first_template(request):
    html_file = open('templates/first_template.html')
    template = Template(html_file.read())
    html_file.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)


def second_template(request):
    return render(request, 'second_template.html')
