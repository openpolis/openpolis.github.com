"""Fabric tasks for publishing a pelican blog to github."""
from __future__ import with_statement

from fabric.api import lcd, local, settings


def pelican():
    """Re-generates the output."""
    # remove all but source from upper dir
    with lcd('..'):
        local('find * -maxdepth 0 ! -name source -print0 | xargs -0n1 rm -rf')
        
    local('pelican . -o ../ -s settings.py')


def push(commit_message):
    """Commits the current changes """
    with lcd('..'):
        local('git add .')
        with settings(warn_only=True):
            local('git commit -am "{0}"'.format(commit_message))
        local('git push origin master')

def publish(commit_message):
    """Re-generates the blog, commits and pushes to github."""
    push(commit_message)
    
    # regenerate output
    pelican()
    
