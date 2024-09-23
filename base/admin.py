from django.contrib import admin
from django.utils.safestring import mark_safe
from django.shortcuts import redirect
# Register your models here.

from .models import Room
from .models import Window



admin.site.register(Room)
admin.site.register(Window)