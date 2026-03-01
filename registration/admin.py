from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'school', 'phone', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['full_name', 'school', 'phone', 'email']
    list_per_page = 25
