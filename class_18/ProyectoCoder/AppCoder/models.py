from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)
    identifier = models.IntegerField()


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    profession = models.CharField(max_length=30)


class Deliverable(models.Model):
    name = models.CharField(max_length=30)
    delivery_date = models.DateField()
    has_been_delivered = models.BooleanField()
