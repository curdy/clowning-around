from django.contrib import admin
from .models import Appointment, AppointmentRate, ReportAppointmentIssue, RequestClientDetailss

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ('appointment_name', 'appointment_date', 'appointment_status', 'clown', 'client_rate_appointment')
    



class AppointmentReportAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'reported_issue')
    
class ContactRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(ReportAppointmentIssue)
admin.site.register(RequestClientDetailss)
admin.site.register(AppointmentRate)