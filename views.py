from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from .models import Bulletin, Events, Student, ScheduleCalendar, FaqMod

from .forms import StudentsForm
# Create your views here.
def index(request):
	#bulletins = Bulletin.objects.order_by('-pk')
	bulletins = Bulletin.objects.order_by('-pub_date')[0:4]
	events = Events.objects.order_by('-pub_date')[0:2]
	if not events:
		events = ['']
	if not bulletins:
		bulletins = ['']
	if request.method == "POST":
		form = StudentsForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			#post.belt_ranking = "W"
			#post.waver_signed = False
			#post.date_joined = timezone.now()
			post.save()
			return HttpResponseRedirect('/thanks/')

	else:
		form = StudentsForm()
	info = {
		"form": form,
		"bulletins": bulletins,
		"events": events,
	}	
	return render(request, 'page/index.html', info)
def about(request):
	bulletins = Bulletin.objects.order_by('-pub_date')[0:4]
	events = Events.objects.order_by('-pub_date')[0:2]
	if not events:
		events = ['']
	if not bulletins:
		bulletins = ['']
	if request.method == "POST":
		form = StudentsForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			#post.belt_ranking = "W"
			#post.waver_signed = False
			#post.date_joined = timezone.now()
			post.save()
			return HttpResponseRedirect('/thanks/')

	else:
		form = StudentsForm()
	info = {
		"form": form,
		"bulletins": bulletins,
		"events": events,
	}	
	return render(request, 'page/about.html', info)

def instructors(request):
	info = {

	}
	return render(request, 'page/instructor.html', info)

def location(request):
	info = {}
	return render(request, 'page/location.html', info)

def schedule(request):
	#Load datetime function check return query of the model, then using python grab the one appropriate to the month
	#Or we can say fuck that and let Mr. Morris set the calendar to active using an admin action. 
	calendar_query = ScheduleCalendar.objects.filter(status="C")
	info = { 
	"current_calendar": calendar_query,
	}
	return render(request, 'page/schedule.html', info)
def faq(request):
	faq_list = FaqMod.objects.all()
	info = {
	"faq": faq_list,
	}
	return render(request, 'page/faq.html', info)
def thanks(request):
	info = {

	}
	return render(request, 'page/thanks.html', info)




