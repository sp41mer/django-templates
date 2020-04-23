from django import forms
from .models import City, School, Student


class SchoolSimpleForm(forms.Form):
    name = forms.CharField()
    number = forms.IntegerField()
    city = forms.IntegerField()


class SchoolForeignKeyForm(forms.Form):
    name = forms.CharField(label="Name")
    number = forms.IntegerField(label="School number")
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="City")


def require_hashtag(value):
    if '#' not in value:
        raise forms.ValidationError("Value must contain a hashtag")


class SchoolWidgetForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.Textarea, validators=[require_hashtag])
    number = forms.IntegerField(label="School number")
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="City")


class SchoolManualForm(forms.Form):
    name = forms.CharField()
    number = forms.IntegerField()
    city = forms.IntegerField()

    def clean_city(self):
        data = City.objects.get(pk=self.cleaned_data['city'])
        return data


class CityField(forms.Field):

    def to_python(self, value):
        return City.objects.get(pk=value)

    def validate(self, value):
        super().validate(value)


class SchoolCustomFieldForm(forms.Form):
    name = forms.CharField()
    number = forms.IntegerField()
    city = CityField()


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


