from django.contrib import admin
from .models import Collecting



# Register your models here.
class CollectingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'marital_status', 'location', 'status', 'email', 'email_password')


admin.site.register(Collecting, CollectingAdmin)
