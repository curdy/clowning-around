from django.db import models
from clowning_around.users.models import Clown, Client, User

class Appointment (models.Model):
    
    STATUS_CHOICES = (
        ('1', 'upcoming',),
        ('2', 'incipient',),
        ('3', 'completed',),
        ('4', 'cancelled',),
    )
    
    appointment_name = models.CharField(max_length=500)
    appointment_date = models.CharField(max_length=50)
    appointment_status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True)
    clown = models.ForeignKey(Clown, null=True, on_delete=models.SET_NULL)
    #client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    
    client_rate_appointment = models.CharField(blank=True, max_length=500)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.appointment_name
    
class ReportAppointmentIssue(models.Model):
    clown = models.ForeignKey(Clown, null=True, on_delete=models.SET_NULL)
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.SET_NULL)
    reported_issue = models.CharField(blank=True, max_length=500)
    def __str__(self):
        return self.appointment
    
class RequestClientDetailss(models.Model):
    request_client_contacts = models.CharField(blank=True, max_length=500)
    request_reason = models.CharField(blank=True, max_length=500)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    clown = models.ForeignKey(Clown, null=True, on_delete=models.SET_NULL)