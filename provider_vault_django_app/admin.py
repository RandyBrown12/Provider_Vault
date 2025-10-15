# Register your models here.
from django.contrib import admin
from .models import Users, Providers

admin.site.register(Users)
admin.site.register(Providers)
