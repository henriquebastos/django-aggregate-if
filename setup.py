# coding: utf-8
from setuptools import setup
import os


setup(name='django-aggregate-if',
      version='0.3',
      description='Conditional aggregates for Django, just like the famous SumIf in Excel.',
      long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
      author="Henrique Bastos", author_email="henrique@bastos.net",
      license="MIT",
      py_modules=['aggregate_if'],
      zip_safe=False,
      platforms='any',
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Database',
          'Topic :: Software Development :: Libraries',
      ],
      url='http://github.com/henriquebastos/django-aggregate-if/',
)
