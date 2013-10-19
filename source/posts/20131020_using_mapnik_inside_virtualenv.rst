Using Mapnik inside a virtualenv on OSX
=======================================

:date: 2013-10-20 10:30
:author: guglielmo
:category: howto
:tags: python, osx, macports


Mapnik_ is a tool to produce maps out of gis data.

.. _Mapnik: https://github.com/mapnik/mapnik/wiki/Mapnik2

Since installation in a virtualenv through ``pip install mapnik2`` fails, due to compilation
problems (boost library cannot be located correctly), the following workaround can be used.

* Install Mapnik through macports::

    sudo port install mapnik @2.2.0_0+python27

  This will install both the libraries and the python bindings, as global packages in::

    /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/

* Link mapnik directories into the virtualenv's site_package directory::

    workon <virtualenv>
    cdsitepackages
    ln -s /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/mapnik .
    ln -s /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/mapnik2 .

