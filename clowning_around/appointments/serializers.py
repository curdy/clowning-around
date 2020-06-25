from rest_framework import serializers
from clowning_around.appointments.models import Appointment, ReportAppointmentIssue, RequestClientDetailss

class AppointmentSerializer(serializers.ModelSerializer): #class that will manage serialization and deserialization from JSON.
    class Meta:
        model = Appointment
        
        fields = "__all__"
        
        def create(self, validated_data):
            return Appointment.objects.create(**validated_data)
            
        
class AppointmentIssueSerializer(serializers.ModelSerializer): #class that will manage serialization and deserialization from JSON.
    class Meta:
        model = ReportAppointmentIssue
        
        fields = "__all__"

class RequestContactSerializer(serializers.ModelSerializer): #class that will manage serialization and deserialization from JSON.
    class Meta:
        model = RequestClientDetailss
        
        fields = "__all__"        