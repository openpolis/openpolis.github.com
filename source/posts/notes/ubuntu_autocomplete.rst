How to configure bash completion in ubuntu
==========================================

:date: 2013-04-11 16:30
:author: guglielmo
:category: howto
:tags: bash, terminal

Working in the terminal of a linux box, the *autocompletion* feature enhances your speed and comfort a lot.

Under Ubuntu, autocompletion is installable, if not already installed, with::

    apt-get install bash_completion
    
The ``~/.bashrc`` config file should contain these lines::

    if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
        . /etc/bash_completion
    fi

If things are set this way, then you will be able to autocomplete regularly (and save a loto of time).

Note:
  In ``/etc/bash_completion.d`` you can find the rather cryptic scripts enabling autocomplete patterns inside various unix contexts.
