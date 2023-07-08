from django.contrib import admin
from .models import SignUp


# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('username', 'email_address', 'password', 'confirm_password')


admin.site.register(SignUp, SignUpAdmin)

