# -*- coding: utf-8 -*-
import os
import json
from django.contrib import admin
from models import List, Value
from django.conf import settings


class ValueInline(admin.TabularInline):
    model = Value


class ListAdmin(admin.ModelAdmin):
    list_display = ('description', 'code',)
    search_fields = ('description', 'code',)
    inlines = (ValueInline,)

    def save_formset(self, request, form, formset, change):
        super(ListAdmin, self).save_formset(request, form, formset, change)

        obj = form.instance
        filename = os.path.join(settings.MEDIA_ROOT, 'values_list',
                                '%s.json' % obj.code)

        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        values = []
        for value in obj.values.all():
            values.append((value.name, value.label))

        with open(filename, 'w+') as outfile:
            json.dump(values, outfile)


admin.site.register(List, ListAdmin)
