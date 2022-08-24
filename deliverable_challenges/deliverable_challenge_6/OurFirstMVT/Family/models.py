from django.db import models


class FamilyMember(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    birthdate = models.DateField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
