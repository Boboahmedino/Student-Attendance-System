from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('attendance', views.attendance, name = 'attendance'),
    path('attendance_history', views.attendance_history, name = 'attendance_history'),
    path('export_pdf', views.export_pdf, name = 'export_pdf'),
    # path('change_password' , views.password, name = 'change_password')
]