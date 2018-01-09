from django.db import models
from django.urls import reverse

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=150)
    principal = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    number_of_students = models.PositiveIntegerField()

    def get_absolute_url(self):
    	return reverse('schools:school_list')

    def __str__(self):
        return self.name + ' - ' + self.location
