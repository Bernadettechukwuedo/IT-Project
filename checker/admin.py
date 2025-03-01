from django.contrib import admin
from .models import Ping

# Register your models here.


class PingAdmin(admin.ModelAdmin):
    list_display = ("url", "status", "timestamp")
    search_fields = ("status", "timestamp")
    list_filter = ("status", "timestamp")


admin.site.register(Ping, PingAdmin)
