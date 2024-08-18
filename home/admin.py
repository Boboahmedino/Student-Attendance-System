from django.contrib import admin
from .models import Attendance, Level, Course, Category
# Register your models here.

admin.site.register(Attendance)
admin.site.register(Level)
admin.site.register(Course)
admin.site.register(Category)