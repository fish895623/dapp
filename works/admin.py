from django.contrib import admin

from .models import Todo, Works, WorkTitle, WorkStatus

# Register your models here.
admin.site.register(Todo)
admin.site.register(Works)
admin.site.register(WorkTitle)
admin.site.register(WorkStatus)
