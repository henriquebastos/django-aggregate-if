#!/usr/bin/env python

import sys
from optparse import OptionParser


def parse_args():
    parser = OptionParser()
    options, args = parser.parse_args()

    # Build labels
    if args:
        labels = ["aggregation.%s" % label for label in args]
    else:
        labels = ['aggregation']

    return options, labels


def configure_settings(options):
    from django.conf import settings

    # If DJANGO_SETTINGS_MODULE envvar exists the settings will be
    # configured by it. Otherwise it will use the parameters bellow.
    if not settings.configured:
        params = dict(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            INSTALLED_APPS = (
                'tests.aggregation',
            ),
            SITE_ID=1,
        )

        # Configure Django's settings
        settings.configure(**params)

    return settings


def get_runner(settings):
    '''
    Asks Django for the TestRunner defined in settings or the default one.
    '''
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)
    return TestRunner(verbosity=1, interactive=True, failfast=False)


def runtests():
    options, test_labels = parse_args()
    settings = configure_settings(options)
    runner = get_runner(settings)
    sys.exit(runner.run_tests(test_labels))


if __name__ == '__main__':
    runtests()
