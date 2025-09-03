from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # doctor urls
    path('add/', views.add_appointment),
    path('update/', views.update_appointment),
    path('get-my-appointments/', views.get_my_appointments),
    # TODO :  path('get-my-appointment/<str:id>/', views.get_my_appointments),
    path('delete/<int:appointment_id>/', views.delete_appointment),
    path('get-scheduled-appointments/',views.get_scheduled_appointments,name='scheduled-appointments'),
    
    # patient urls
    path('take-appointment/', views.take_appointment, name='take-appointment'),
    path('cancel-appointment/', views.cancel_appointment),
    path('get-patient-appointments/', views.get_patient_appointments),
    # TODO : path('get-patient-appointment/<str:id>/', views.get_patient_appointments),
]
