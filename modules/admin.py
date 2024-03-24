from django.contrib import admin
from modules.models import Module


@admin.register(Module)
class StudyUnitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'education_time')
    list_filter = ('name',)
