"""Settings for pelican."""
import os

AUTHOR = u'Openpolis'
SITENAME = u'Openpolis Lab'
SITEURL = 'http://openpolis.github.com'
TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Openpolis', 'http://www.openpolis.it'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/openpolis'),
          ('twitter', 'https://twitter.com/openpolis'),
          ('github', 'https://github.com/openpolis/'),)

DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True

# clone pelican-themes from github onto your hard disk
PELICAN_THEMES_PATH = '/Users/guglielmo/Workspace/pelican-themes/'
THEME = os.path.join(PELICAN_THEMES_PATH, 'tuxlite_tbs')

# setting this, activates the DISQUS comments
DISQUS_SITENAME = 'openpolislab'

GITHUB_URL = 'http://github.com/openpolis/openpolis.github.com'
TWITTER_USERNAME = 'guille'

# to activate typogrify
TYPOGRIFY = True


# I like to have ``Archives`` in the main menu.
MENUITEMS = (
    ('Archives', 'archives.html'),
)




# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
#DISQUS_SITENAME = 'yourdisqushandle'
