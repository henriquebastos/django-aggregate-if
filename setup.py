# coding: utf-8
from setuptools import setup, find_packages
import os


setup(name='django-aggregate-if',
      version='0.1',
      description='Conditional aggregates for Django, just like the famous SumIf in Excel.',
      long_description=open(os.path.join(os.path.dirname(__file__), "README.txt")).read(),
      author="Henrique Bastos", author_email="henrique@bastos.net",
      license="MIT",
      packages=find_packages(exclude=["tests*"]),
      classifiers=[
          'Development Status :: 4 - Beta',
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
