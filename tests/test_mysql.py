# coding: utf-8

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aggregation',
    }
}

INSTALLED_APPS = (
    'tests.aggregation',
)

SITE_ID=1,

SECRET_KEY='secret'
