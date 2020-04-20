from django.shortcuts import render
from school.models import School
from school.forms import SchoolForm


def all_schools(request):
    schools = School.objects.all()
    return render(request, 'all_schools.html', context={"schools": schools})


def show_school(request, pk):
    school = School.objects.get(pk=pk)
    form = SchoolForm(instance=school)
    return render(request, 'show_school.html', context={"form": form})


def create_school(request):
    if request.method == 'GET':
        form = SchoolForm()
        return render(request, 'create_school.html', context={"form": form})
    elif request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'create_school.html', context={"form": form})


def delete_school(request, pk):
    if request.method == 'GET':
        school = School.objects.filter(pk=pk).first()
        form = SchoolForm(instance=school)
        return render(request, 'delete_school.html', context={"form": form})
    elif request.method == 'POST':
        form = SchoolForm()
        school = School.objects.filter(pk=pk).first()
        if school:
            school.delete()
        return render(request, 'delete_school.html', context={"form": form})


def edit_school(request, pk):
    if request.method == 'GET':
        school = School.objects.get(pk=pk)
        form = SchoolForm(instance=school)
        return render(request, 'update_school.html', context={"form": form})
    elif request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'update_school.html', context={"form": form})
