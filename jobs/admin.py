from django.contrib import admin

from .models import Job, JobLevelOne, JobLevelTwo, JobAblityShip


class JobAblityInline(admin.TabularInline):
    model = JobAblityShip
    extra = 1


class JobAdmin(admin.ModelAdmin):
    inlines = (JobAblityInline,)


admin.site.register(Job, JobAdmin)
admin.site.register(JobLevelOne)
admin.site.register(JobLevelTwo)
