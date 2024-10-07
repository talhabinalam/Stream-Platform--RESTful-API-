from django.contrib import admin
from .models import *


class WatchListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'active', 'created')
    ordering = ['id']


admin.site.register(WatchList, WatchListAdmin)
admin.site.register(StreamPlatform)
admin.site.register(Review)
