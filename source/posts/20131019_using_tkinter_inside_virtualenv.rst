Using Tkinter inside a virtualenv
=================================

:date: 2013-10-19 10:30
:author: guglielmo
:category: howto
:tags: python, osx, macports


Tkinter_ is usually installed on OSX trhough macports_ as a global package::

    sudo port install py27-tkinter
    
Within a virtualenv the package will not be imported, as global packages are not included by default::

    >>> import Tkinter
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/Tkinter.py", line 39, in <module>
        import _tkinter # If this fails your Python may not be configured for Tk
    ImportError: No module named _tkinter

The package consists of a single library (_tkinter.so) and can be installed in the virtualenv by symlinking::

    ln -s /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/_tkinter.so .
    
.. _Tkinter: https://wiki.python.org/moin/TkInter
.. _macports: http://www.macports.org/
