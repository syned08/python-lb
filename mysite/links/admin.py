from django.contrib import admin

from .models import Links, Categories, Authors


class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'count_visites')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_description')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name', )


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name', 'country', 'age')
    list_display_links = ('id', 'first_name', 'second_name')
    search_fields = ('first_name', 'second_name')


admin.site.register(Links, LinksAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Authors, AuthorsAdmin)
