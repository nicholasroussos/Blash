from django import forms
from .models import Student

class StudentsForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('first_name', 'last_name', 'phone_number', 'student_email', 'class_choice')