"""Fabric tasks for publishing a pelican blog to github."""
from __future__ import with_statement

from fabric.api import lcd, local, settings


def pelican():
    """Re-generates the output."""
    # remove all but source from upper dir
    with lcd('..'):
        local('find * -maxdepth 0 ! -name source -print0 | xargs -0n1 rm -rf')
        
    local('pelican . -o ../ -s settings.py')


def push():
    """Commits the current changes """
    with lcd('..'):
        local('git add . && git commit')
        local('git push origin master')

def publish():
    
    # regenerate output
    pelican()

    """Re-generates the blog, commits and pushes to github."""
    push()
    
