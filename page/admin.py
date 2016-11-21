from django.contrib import admin

# Register your models here.
from .models import Student, Bulletin, Events, ScheduleCalendar, FaqMod

def make_current(modeladmin, request, queryset):
	queryset.update(status="C")
	make_current.short_description = "Change the current calendar to this month."
def make_irrelevant(modeladmin, request, queryset):
	queryset.update(status="I")
	make_irrelevant.short_description = "Change a calendar to irrelevant"

class StudentAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'student_email', 'belt_ranking', 'wavier_signed', 'date_joined']
	class Meta:
		model = Student

class BulletinAdmin(admin.ModelAdmin):
	list_display = ['pub_date', 'new_announcement']
	class Meta:
		model = Bulletin

class EventsAdmin(admin.ModelAdmin):
	list_display = ['new_event', 'event_date', 'event_description', 'pub_date']
	class Meta:
		model = Events
class CalendarAdmin(admin.ModelAdmin):
	list_display = ['calendar_month', 'status', 'pub_date', 'schedule_calendar']
	actions = [make_current, make_irrelevant]
	class Meta: 
		model = ScheduleCalendar
class FaqAdmin(admin.ModelAdmin):
	list_display = ['question', 'answer']
	class Meta:
		model = FaqMod

admin.site.register(Student, StudentAdmin)
admin.site.register(Bulletin, BulletinAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(ScheduleCalendar, CalendarAdmin)
admin.site.register(FaqMod, FaqAdmin)