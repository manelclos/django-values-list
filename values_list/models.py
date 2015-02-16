import os
import json
from django.db import models
from django.conf import settings


class List(models.Model):
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(List, self).save(*args, **kwargs)
        filename = os.path.join(settings.MEDIA_ROOT, 'values_list',
                                '%s.json' % self.code)

        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        values = []
        for value in self.values.all():
            values.append((value.name, value.label))

        with open(filename, 'wb') as outfile:
            json.dump(values, outfile)


class Value(models.Model):
    list = models.ForeignKey(List, related_name='values')
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        unique_together = ('list', 'name')
