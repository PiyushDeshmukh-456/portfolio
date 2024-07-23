from django.contrib import admin
from .models import Project, Resume

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')  # Fields to display in the list view
    search_fields = ('title', 'description')  # Fields to search in the admin panel
    list_filter = ('title',)  # Optional: Add filters to the admin panel

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')  # Fields to display in the list view
    search_fields = ('title',)  # Fields to search in the admin panel
