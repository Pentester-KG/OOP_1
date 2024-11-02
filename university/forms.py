from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentSearchForm(forms.Form):
    student_id = forms.CharField(label="Номер студенческого билета", max_length=20)
