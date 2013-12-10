Writeable Foreign keys in Django Rest Framework
===============================================

:date: 2013-12-09 10:45
:author: guglielmo
:category: howto
:tags: python, django, django-rest-framework, API

`Django Rest Framework`_ is a django-based framework to produce browseable APIs.

.. _`Django Rest Framework`: http://django-rest-framework.org/

The documentation and the tutorial are pretty much clear, but implementing a writeable API
for related fields can be tricky.

RelatedField is read-only.
PrimaryKeyRelatedFields, HyperlinkedRelatedField, SlugRelatedField, can be used as writeable, but the 
related items must already exist. It seems they're more appropriate to handle aggregation relations (i.e. User and Groups)

Nested relationships can be used to handle composition relations (i.e. a Place and its Acronyms). 
The quirk is that the get_identity() method must be re-written in the nested serializer, because the default one uses 
the id field to determine the identity of the items, which may not have, and which you surely don't have when creating new items.

A working example with Places and Acronyms can be found `here`_.

.. _`here`: http://gist.github.com/guglielmo/7851650


Given a Place instance with just one acronym, the JSON representation would be::

    {
        "_self": "http://localhost:8003/maps/places/roma-comune", 
        "slug": "roma-comune", 
        "name": "Roma", 
        "acronyms": [
            "RM"
        ]
    }


PUTting the following json payload to the resource::

    {
        "slug": "roma-comune", 
        "name": "Roma", 
        "acronyms": [
            "RM", "ROM"
        ]
    }

or PATCHing the even shorter one::

    {
        "acronyms": [
            "RM", "ROM"
        ]
    }
  
The final result would be that the **ROM** acronym would be added to the Place resource.


