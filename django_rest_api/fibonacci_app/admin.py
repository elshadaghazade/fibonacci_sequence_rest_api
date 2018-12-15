from django.contrib import admin
from .models import Logs

class LogsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Logs, LogsAdmin)
