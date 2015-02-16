# django-values-list
Easy CHOICES in Database when you don't want/need to create one zillion tables and Foreign Keys

Use it when you want some user/admin to add/update the list of values.

Usage
-----

Add ''values_list'' to INSTALLED_APPS.

Add ''MyListCode'' list values using the admin.

Use it in your model:
```
from values_list.utils import get_cached_values

class MyModel(models.Model):
    choice = models.CharField(max_length=100, choices=get_cached_values('MyList_code'),
```

Note: since the model is cached, refreshing the values requires an application restart.
