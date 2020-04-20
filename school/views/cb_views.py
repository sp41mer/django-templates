from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView
from django.views.generic.base import View
from django.views.generic.list import ListView

from school.forms import SchoolForm
from school.models import School


class CreateSchoolView(View):

    def get(self, request):
        form = SchoolForm()
        return render(request, 'create_school.html', context={"form": form})

    def post(self, request):
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'create_school.html', context={"form": form})


class AllSchoolsTemplateView(TemplateView):

    template_name = 'all_schools.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schools = School.objects.all()
        context.update({"schools": schools})

        return context


class SchoolDetailView(DetailView):

    model = School


class SchoolCreateView(CreateView):

    model = School
    fields = '__all__'
    success_url = '/cb_all_template/'

    def get_success_url(self):
        return '/cb_detail/{}/'.format(self.object.pk)


class SchoolsListView(ListView):

    model = School
    context_object_name = 'schools'
    paginate_by = 10
