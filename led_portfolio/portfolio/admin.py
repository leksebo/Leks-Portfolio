from django.contrib import admin
from .models import Project, PersonalInfo
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured')
    list_filter = ('is_featured',)
    formfield_overrides = {
        HTMLField: {'widget': TinyMCE()},
    }

class PersonalInfoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        HTMLField: {'widget': TinyMCE()},
    }

admin.site.register(Project, ProjectAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
