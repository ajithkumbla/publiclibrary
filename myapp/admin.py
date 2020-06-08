from django.contrib import admin
from .models import *

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('library','title','author','updated_on','content','created_on','status')
    list_filter = ('status',)
    search_fields = ('title', 'author')
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(status=True)
    
admin.site.register(Library)
admin.site.register(Post,CommentAdmin)