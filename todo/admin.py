from django.contrib import admin
from .models import TodoItem


class TodoItemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'description', 'status')
        }),
        ('Additional Information', {
            'fields': ('due_date', 'tags')
        }),
        ('Timestamp', {
            'fields': ('timestamp',),
            'classes': ('collapse',)
        }),
    )
    list_display = ('title', 'description', 'due_date', 'status')
    list_filter = ('status', 'tags', 'due_date')  

admin.site.register(TodoItem, TodoItemAdmin)