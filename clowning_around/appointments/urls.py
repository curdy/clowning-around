from django.conf.urls import url
from django.urls import path
from clowning_around.appointments import views

app_name = "appointments"

urlpatterns = [
    path('api/appointments/<str:id>', views.AppointmentDetail.as_view(), name="detail"),
    url(r'^api/appointments$', views.AppointmentList.as_view(), name="appointments"),
]
