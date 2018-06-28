from django.contrib import admin

from .models import Job, JobLevelOne, JobLevelTwo

admin.site.register(Job)
admin.site.register(JobLevelOne)
admin.site.register(JobLevelTwo)
