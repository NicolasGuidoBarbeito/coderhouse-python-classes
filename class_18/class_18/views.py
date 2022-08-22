from datetime import datetime

from django.shortcuts import render


def first_template(request):
    context = {
        "current_date_time": datetime.now(),
        "first_name": "Ezequiel",
        "last_name": "Bálsamo",
        "age": 26
    }

    return render(request, 'first_template.html', context)


def second_template(request, first_name, last_name, age):
    context = {
        "current_date_time": datetime.now(),
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "favourite_programming_languages": ["Smalltalk", "Javascript", "Python"]
    }
    return render(request, 'first_template.html', context)

