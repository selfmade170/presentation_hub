from django.contrib import admin
from .models import Presentation

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ("title", "school_class", "uploaded_at", "file")
    list_filter = ("school_class", "uploaded_at")   # фильтры сбоку
    search_fields = ("title", "description")        # поиск по названию и описанию
