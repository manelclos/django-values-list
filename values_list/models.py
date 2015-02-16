import os
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.conf import settings

class List(models.Model):
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank=True)

@receiver(post_delete, sender=List)
def auto_delete_file_on_delete(sender, instance, **kwargs):

    filename = os.path.join(settings.MEDIA_ROOT, 'values_list',
                            '%s.json' % instance.code)
    if os.path.isfile(filename):
        os.unlink(filename)   

class Value(models.Model):
    list = models.ForeignKey(List, related_name='values')
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        unique_together = ('list', 'name')
