# coding: utf-8

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'tests.aggregation',
)

SITE_ID=1,

SECRET_KEY='secret'
