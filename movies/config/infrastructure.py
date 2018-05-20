# -*- coding: utf-8 -*-
import json
import os
configPath = os.environ.get('DJANGODBCONFIG') if 'DJANGODBCONFIG' in os.environ else 'config/data/infrastructure.json'
try:
    database_config = open(configPath).read()
    DATABASES = json.loads(database_config)
except:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(__file__, 'db.sqlite3'),
        }
    }
