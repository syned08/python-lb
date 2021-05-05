from django.contrib import admin

from .models import Links

class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'count_visites')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')


admin.site.register(Links, LinksAdmin)