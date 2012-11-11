:date: 2012-11-10
:author: guglielmo
:category: blog
:tags: pelican, python
:slug: about-this-blog
:lang: en
:title: About this blog

This is the technical blog here at Openpolis_. It hosts articles written by our technical staff, while facing and possibly solving problems during the day to day operations.

It is a pelican_-based blog and we write the articles as simple Markdown_ or ReStructured_ text files.



Installation
============
You can install this solution for yourself.
Fork ``git@github.com:openpolis/openpolis.github.com.git`` to your github account.
Use the ``git@github.com:[account]/[account].github.com.git`` naming convention to have the
html pages hosted automagically on `github's user or organization pages`__ at ``http://[account].github.com``.

__ https://help.github.com/articles/user-organization-and-project-pages

Now, follow these instructions:

.. sourcecode:: sh

    $ mkvirtualenv [YOUR BLOG NAME]
    $ git clone [YOUR GIT FORK] [YOUR BLOG NAME]
    $ cd [YOUR BLOG NAME]/source
    $ setvirtualenvproject
    $ pip install -r requirements
    

Read the ``settings.py`` file, to adapt the blog to your context.
You can select one among a set of pre-default themes, as a starting point for your customisations.
You can activate the disqus_ comments, tipogrify_ enhancements, google analytics, twitter and github links.

Usage
=====
To rebuild the html code:

.. sourcecode:: sh

    $ fab pelican

to publish the html to github:

.. sourcecode:: sh

    $ fab push
    
to compile and push at once:

.. sourcecode:: sh

    $ fab publish
  
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

Activating the virtualenv with ``workon``, places you **inside** the source folder, where the ``fabfile.py`` file lives.
That enables you to use the ``fab`` tasks.

Note that the output folder is above the source folder. All output is removed before a rebuild, 
the source directory is excluded and the CNAME file, needed by github is re-generated. 
This is obtained through this ``fab`` code in the ``pelican`` task:

.. sourcecode:: python

    with lcd('..'):
      local('find * -maxdepth 0 ! -name source -print0 | xargs -0n1 rm -rf')
      local('touch CNAME; echo lab.openpolis.it >> CNAME')


    
.. _Openpolis: http://www.openpolis.it
.. _pelican: https://github.com/getpelican/pelican
.. _Markdown: http://daringfireball.net/projects/markdown/syntax
.. _ReStructured: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _github: 
.. _disqus: http://disqus.com/
.. _tipogrify: http://jeffcroft.com/blog/2007/may/29/typogrify-easily-produce-web-typography-doesnt-suc/
.. _Fabric: https://github.com/fabric/fabric

