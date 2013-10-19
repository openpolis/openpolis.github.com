"""Fabric tasks for publishing a pelican blog to github."""
from __future__ import with_statement

from fabric.api import lcd, local, settings


def pelican(reload_mode=False):
    """Re-generates the output."""
    # remove all but source from upper dir
    # re-generate CNAME
    with lcd('..'):
        local('find * -maxdepth 0 ! -name source -print0 | xargs -0n1 rm -rf')
        local('touch CNAME; echo lab.openpolis.it >> CNAME')

    if reload_mode:
        local('pelican . -o ../ -r -s settings.py')
    else:
        local('pelican . -o ../ -s settings.py')


def push():
    """Commits the current changes """
    with lcd('..'):
        local('git add .')
        local('git commit m "pushed"')
        local('git push origin master')

def publish():
    
    # regenerate output
    pelican()

    """Re-generates the blog, commits and pushes to github."""
    push()
    
