from django.contrib import admin
from models import List, Value


class ValueInline(admin.TabularInline):
    model = Value


class ListAdmin(admin.ModelAdmin):
    list_display = ('description', 'code',)
    search_fields = ('description', 'code',)
    inlines = (ValueInline,)

admin.site.register(List, ListAdmin)
