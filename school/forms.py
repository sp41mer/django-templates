from django.forms import ModelForm
from .models import City, School, Student


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
