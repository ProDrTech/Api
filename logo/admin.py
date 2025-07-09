from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('logo',)
    actions = ['delete_selected']  # Delete tugmasini ko‘rsatadi
