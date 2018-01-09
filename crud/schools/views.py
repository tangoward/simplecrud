from django.shortcuts import render
from .models import School
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class SchoolList(ListView):
    model = School
    context_object_name = 'schools'
    template_name = 'schools/school_list.html'


class SchoolDetail(DetailView):
    model = School
    context_object_name = 'schools'
    template_name = 'schools/school_detail.html'


class SchoolCreate(CreateView):
    model = School
    fields = ('name', 'location', 'principal', 'number_of_students')
    template_name = 'schools/school_create.html'


class SchoolUpdate(UpdateView):
    model = School
    fields = ('location', 'principal', 'number_of_students')
    template_name = 'schools/school_update.html'


class SchoolDelete(DeleteView):
    model = School
    success_url = reverse_lazy('schools:school_list')
    template_name = 'schools/school_delete.html'
