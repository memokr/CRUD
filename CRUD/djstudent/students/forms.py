from django import forms
from students.models import Student
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= "__all__"