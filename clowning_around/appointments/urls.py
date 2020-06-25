from django.conf.urls import url
from django.urls import path
from clowning_around.appointments import views

app_name = "appointments"

urlpatterns = [
    path('api/appointments/<str:id>', views.AppointmentDetail.as_view(), name="detail"),
    url(r'^api/appointments$', views.AppointmentList.as_view(), name="appointments"),
    url(r'^api/request-contact$', views.RequestContact.as_view(), name="request"),
    url(r'^api/log-ticket$', views.LogIssueTicket.as_view(), name="tiecket"),
]
