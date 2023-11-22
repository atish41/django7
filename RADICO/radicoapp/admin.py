from django.contrib import admin
from .models import startups
# Register your models here.
class startup_admin(admin.ModelAdmin):
    list_display = ['startup_no','startup_name','startup_domain','startup_city']



admin.site.register(startups,startup_admin)