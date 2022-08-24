from datetime import datetime

from django.shortcuts import render
from .models import FamilyMember


def family_members(request):
    context = {
        'family_members': FamilyMember.objects.all()
    }

    return render(request, 'index.html', context)


def family_member_registration(request, first_name: str, last_name: str, age: int, birthdate_as_string: str):
    birthdate = datetime.strptime(birthdate_as_string, "%Y-%m-%d").date()
    family_member = FamilyMember(first_name=first_name, last_name=last_name, age=age, birthdate=birthdate)
    family_member.save()
    context = {
        'family_member': family_member
    }

    return render(request, 'family_member_registration.html', context)
