from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Student(models.Model):
	first_name = models.CharField(max_length=100, default='' )
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	last_name = models.CharField(max_length=100, default='')
	student_email = models.EmailField(max_length=120, default='', blank="True")
	class_options = (
		('C', "Child"),
		('A', "Adult"),
		)
	belt_choices = (
		('W', "White"),
		('Y', "Yellow"),
		('G', "Green"),
		('Br', "Brown"),
		('Pr', "Purple"),
		('R', "Red"),
		('Bk', "Black"),
		('Bl', "Blue"),
		)
	class_choice = models.CharField(max_length=10, choices=class_options, default='C')
	belt_ranking = models.CharField(max_length=120, choices=belt_choices, default='W')
	phone_number = models.CharField(validators=[phone_regex], default="", max_length=16,)
	wavier_signed = models.BooleanField(default=False)
	date_joined = models.DateTimeField(auto_now_add=True, auto_now = False, blank='True')


class Bulletin(models.Model):
	new_announcement = models.TextField(default='Enter text here...')
	pub_date = models.DateTimeField(auto_now_add=True, auto_now = False)

class Events(models.Model):
	new_event = models.CharField(max_length=140, default='Enter event title here...')
	event_description = models.TextField(default='Enter text here')
	event_date = models.DateTimeField()
	pub_date = models.DateTimeField(auto_now_add=True, auto_now = False)

	class Meta: 
		verbose_name = "Event"

#intended for depositing latest schedule calendar.
class ScheduleCalendar(models.Model):
	status_choices = (
		('C', "Current"),
		('I', "Irrelevent"),
		)
	status = models.CharField(max_length=1, choices=status_choices, default="I",)
	pub_date = models.DateTimeField(auto_now_add=True, auto_now = False)
	calendar_month = models.DateField()
	schedule_calendar = models.FileField(upload_to='schedule_calendar', default='', null="True", blank="True")
class FaqMod(models.Model):
	question = models.TextField(default="Enter question here....", )
	answer = models.TextField(default="Enter answer here....",)
	class Meta: 
		verbose_name = "FAQ"