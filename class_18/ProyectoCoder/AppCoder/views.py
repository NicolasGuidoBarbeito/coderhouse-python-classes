from django.shortcuts import render

from .models import Course


def create_course(request, course_name, course_identifier):
    course = Course(name=course_name, identifier=course_identifier)
    course.save()
    context = {
        'course': course
    }

    return render(request, 'course_creation.html', context)


def courses(request):
    context = {
        'courses': Course.objects.all()
    }

    return render(request, 'courses.html', context)
