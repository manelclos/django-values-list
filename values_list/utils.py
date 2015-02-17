import os
import json
from django.conf import settings


def get_cached_values(code):
    filename = os.path.join(settings.MEDIA_ROOT, 'values_list',
                            '%s.json' % code)

    if os.path.exists(filename):
        with open(filename) as data_file:
            values = json.load(data_file)
            return values

    return []
