from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, YearArchiveView
from django.views.generic.base import View
from django.views.generic.list import ListView

from school import forms
from school.forms import SchoolForm, StudentForm, SchoolSimpleForm, SchoolForeignKeyForm
from school.models import School, Student, City


class CreateSchoolView(View):

    form = forms.SchoolCustomFieldForm

    def get(self, request):
        form = self.form()
        return render(request, 'create_school.html', context={"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            # city = City.objects.get(pk=form.cleaned_data.pop('city'))
            School.objects.create(**form.cleaned_data)
        return render(request, 'create_school.html', context={"form": form})


class CreateStudentView(View):

    form = StudentForm

    def get(self, request):
        form = self.form()
        return render(request, 'create_student.html', context={"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'create_student.html', context={"form": form})



class AllSchoolsTemplateView(TemplateView):

    template_name = 'all_schools.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schools = School.objects.all()
        context.update({"schools": schools})

        return context


class AllStudentsTemplateView(TemplateView):

    template_name = 'all_students.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = Student.objects.all()
        context.update({"students": students})

        return context


class SchoolDetailView(DetailView):

    model = School


class StudentDetailView(DetailView):

    model = Student


class SchoolCreateView(CreateView):

    model = School
    fields = '__all__'
    success_url = '/cb_all_template/'

    def get_success_url(self):
        return '/cb_detail/{}/'.format(self.object.pk)


class StudentCreateView(CreateView):

    model = Student
    fields = '__all__'
    success_url = '/cb_all_students/'

    def get_success_url(self):
        return '/cb_student_detail/{}/'.format(self.object.pk)


class SchoolsListView(YearArchiveView):

    model = School
    context_object_name = 'schools'
    paginate_by = 10


class StudentListView(ListView):

    model = Student
    context_object_name = 'students'
    paginate_by = 10
