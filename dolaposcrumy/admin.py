from django.contrib import admin
from .models import ScrumyGoals, ScrumyUser, ScrumyStatus

# Register your models here.

admin.site.register(ScrumyUser)
admin.site.register(ScrumyGoals)
admin.site.register(ScrumyStatus)
