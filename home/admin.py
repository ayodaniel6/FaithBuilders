from django.contrib import admin
from .models import Client, Newsletter, Request

# Register your models here.

admin.site.register(Client)
admin.site.register(Newsletter)
admin.site.register(Request)
