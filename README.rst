Django Aggregate If: Condition aggregates for Django
====================================================

.. image:: https://travis-ci.org/henriquebastos/django-aggregate-if.png?branch=master
        :target: https://travis-ci.org/henriquebastos/django-aggregate-if

*Aggregate-if* adds conditional aggregates to Django.

Conditional aggregates can help you reduce the ammount of queries to obtain
aggregated information, like statistics for example.

Imagine you have a model ``Offer`` like this one:

.. code-block:: python

    class Offer(models.Model):
        sponsor = models.ForeignKey(User)
        price = models.DecimalField(max_digits=9, decimal_places=2)
        status = models.CharField(max_length=30)
        expire_at = models.DateField(null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        OPEN = "OPEN"
        REVOKED = "REVOKED"
        PAID = "PAID"

Let's say you want to know:

#. How many offers exists in total;
#. How many of them are OPEN, REVOKED or PAID;
#. How much money was offered in total;
#. How much money is in OPEN, REVOKED and PAID offers;

To get these informations, you could query:

.. code-block:: python

    from django.db.models import Count, Sum

    Offer.objects.count()
    Offer.objects.filter(status=Offer.OPEN).aggregate(Count('pk'))
    Offer.objects.filter(status=Offer.REVOKED).aggregate(Count('pk'))
    Offer.objects.filter(status=Offer.PAID).aggregate(Count('pk'))
    Offer.objects.aggregate(Sum('price'))
    Offer.objects.filter(status=Offer.OPEN).aggregate(Sum('price'))
    Offer.objects.filter(status=Offer.REVOKED).aggregate(Sum('price'))
    Offer.objects.filter(status=Offer.PAID).aggregate(Sum('price'))

In this case, **8 queries** were needed to retrieve the desired information.

With conditional aggregates you can get it all with only **1 query**:

.. code-block:: python

    from django.db.models import Q
    from aggregate_if import Count, Sum

    Offer.objects.aggregate(
        Count('pk'),
        Count('pk', only=Q(status=Offer.OPEN)),
        Count('pk', only=Q(status=Offer.REVOKED)),
        Count('pk', only=Q(status=Offer.PAID)),
        Sum('price'),
        Sum('price', only=Q(status=Offer.OPEN)),
        Sum('price'), only=Q(status=Offer.REVOKED)),
        Sum('price'), Q(status=Offer.PAID)),
    )

Installation
------------

To install django-aggregate-if, simply:

.. code-block:: bash

    $ pip install django-aggregate-if

Inspiration
-----------

There is a `ticket 11305`_ that will (*hopefully*) implement this feature into
Django 1.6.

Using Django 1.4, I still wanted to avoid creating custom queries for very simple
conditional aggregations. So I've cherry picked those ideas and others from the
internet and built this library.

This library uses the same API and tests proposed on `ticket 11305`_, so when the
new feature is available you can easily replace ``django-aggregate-if``.

Limitations
-----------

Conditions involving joins with aliases are not supported yet. If you want to
help adding this feature, you're welcome to check the `first issue`_.

License
=======

The MIT License.

.. _ticket 11305: https://code.djangoproject.com/ticket/11305
.. _first issue: https://github.com/henriquebastos/django-aggregate-if/issues/1
