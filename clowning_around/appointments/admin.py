from django.contrib import admin
from .models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ('appointment_name', 'appointment_date', 'appointment_status', 'clown', 'client_rate_appointment')
    list_filter = ('appointment_status', 'clown')  # The list_filter option
    #ordering = ('appointment_date',)
    search_fields = (
    'appointment_name', 'appointment_status')  # sets the default search fields.



class AppointmentReportAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'reported_issue')
    
class ContactRequestAdmin(admin.ModelAdmin):
    pass