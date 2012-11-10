###############
ABOUT THIS BLOG
###############

:date: 2012-11-10
:author: guglielmo
:category: blog pelican

This is the technical blog here at Openpolis_. It hosts articles written by our technical staff, while facing and possibly solving problems during the day to day operations.

It is a pelican_-based blog and we write the articles as simple Markdown_ or ReStructured_ text files.



Installation
============
Fork ``git@github.com:openpolis/openpolis.github.com.git`` to your github account.

Use the ``git@github.com:[account]/[account].github.com.git`` naming convention to have the
html pages hosted automagically on github at ``http://[account].github.com``.

Follow these instructions::

    mkvirtualenv [YOUR BLOG NAME]
    git clone [YOUR GIT FORK] [YOUR BLOG NAME]
    cd [YOUR BLOG NAME]/source
    setvirtualenvproject
    pip install -r requirements
    

Read the ``settings.py`` file, to adapt the blog to your context.
You can select one among a set of pre-default themes, as a starting point for your customisations.
You can activate the disqus_ comments, tipogrify_ enhancements, google analytics, twitter and github links.

Usage
=====
To rebuild the html code::

    fab pelican

to publish the html to github::

    fab push
    
to compile and push at once::

    fab publish
  
Notes
=====

This is the directory tree::
  
    ./
    |- CNAME
    |- index.html
    |- author
    |  |- guglielmo.html
    |  |- danielef.html
    |- categories.html
    |- category
    |  |- python.html
    |  |- rest-api.html
    | ...
    |- source
       |- fabfile.py
       |- requirements.txt
       |- settings.py
       |- README.rst
       |- first.post.rst
    
Fabric_ is used to manage the 'compile/push/publish' tasks.

Activating the virtualenv with ``workon``, places you inside the source folder, where the ``fabfile.py`` file lives.
That enables you to use the ``fab`` tasks.

Note that the output folder is above the source folder. All output is removed before a rebuild, 
the source directory is excluded. This is obtained through this ``fab`` task

.. sourcecode:: python

    with lcd('..'):
      local('find * -maxdepth 0 ! -name source -print0 | xargs -0n1 rm -rf')
      local('touch CNAME; echo lab.openpolis.it >> CNAME')
    
launched on the output directory.


    
.. _Openpolis: http://www.openpolis.it
.. _pelican: https://github.com/getpelican/pelican
.. _Markdown: http://daringfireball.net/projects/markdown/syntax
.. _ReStructured: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _disqus: http://disqus.com/
.. _tipogrify: http://jeffcroft.com/blog/2007/may/29/typogrify-easily-produce-web-typography-doesnt-suc/
.. _Fabric: https://github.com/fabric/fabric

