from django.contrib import admin
from .models import Department, GirlStudent, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(GirlStudent)

