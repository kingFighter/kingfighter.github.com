#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# window
from __future__ import unicode_literals
from os import getenv

AUTHOR = 'kingFighter'
SITENAME = "kingFighter's Nest"
SITEURL = '//' + getenv("SITEURL", default='localhost:8000')
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'
LOCALE = 'en'
#LOCALE = 'zh_CN.UTF8'


DATE_FORMATS = {
    'en': ('english', '%a, %d %b %Y',),
    'zht': ('chinese', '%Y年%m月%d日(週%a)',),
    'zh': ('chinese','%Y年%m月%d日(周%a)',),
    'ja': ('japanese', '%Y年%m月%d日(%a曜日)',),
}

DISQUS_SITENAME = 'kingfighter'
DISQUS_DISPLAY_COUNTS = True
GOOGLE_ANALYTICS = 'UA-40492618-1'

# Feed generation is usually not desired when developing
TAG_FEED_ATOM = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 12

STATIC_PATHS = ['static',
                'images',
                'uml',
                'images/favicon.ico',
                'static/CNAME']

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'static/CNAME': {'path': 'CNAME'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/manifest.json': {'path': 'manifest.json'},
    'static/browserconfig.xml': {'path': 'browserconfig.xml'},
    'static/keybase.txt': {'path': 'keybase.txt'},
}

PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

PLUGIN_PATHS = ['plugins']
THEME = "theme"


I18N_SUBSITES = {
    # 'ja': dict(
    #     LOCALE='japanese',
    #     SITENAME="kingFighterの巣",
    #     STATIC_PATHS=STATIC_PATHS
    # ),
    # 'en': dict(
    #     LOCALE='english',
    #     SITENAME="kingFighter's Nest",
    #     STATIC_PATHS=STATIC_PATHS
    # ),
    # 'zht': dict(
    #     LOCALE='chinese',
    #     SITENAME="kingFighter的小窩",
    #     STATIC_PATHS=STATIC_PATHS
    # ),
    'zh': dict(
        LOCALE='chinese',
        SITENAME="kingFighter的小窝",
        STATIC_PATHS=STATIC_PATHS
    ),
}

I18N_UNTRANSLATED_ARTICLES = "remove"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums':'False'},
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.toc': {},
    },
}

PLUGINS = ["i18n_subsites",
           "better_codeblock_line_numbering",
           "plantuml",
#           "youku",
#           "pelican_youtube",
           'tipue_search',
           'neighbors',
           'series',
           'bootstrapify',
           'twitter_bootstrap_rst_directives',
           "render_math",
           'extract_toc',
           'tag_cloud',
           'sitemap',
           'summary']

SITEMAP = {
    'format': 'xml',
}

USE_LESS = False

# # Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
CHECK_MODIFIED_METHOD = "md5"
LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True

# # Theme options

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']} 


DOCUTIL_CSS = True
TYPOGRIFY = False
PYGMENTS_STYLE = 'monokai'
GITHUB_USER = 'kingFighter'
GITHUB_SHOW_USER_LINK = True
GITHUB_REPO = 'kingFighter/kingFighter.github.io'
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
CC_LICENSE = "CC-BY-NC-SA"
DISPLAY_TAGS_INLINE = True
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = '.rst'

# WEIBO_WIDGET = True
# WEIBO_APPKEY = "NANnN"
# WEIBO_APPKEYN = "498769639"

DIRECT_TEMPLATES = (('search', 'index', 'categories', 'authors', 'archives',
                     'tags'))

# TWITTER_USERNAME = 'farseerfc'
# TWITTER_WIDGET_ID = "538997172142759936"

AVATAR = 'images/avatar.jpg'
ABOUT_PAGE = "about.html"
ABOUT_ME = """<h3 style="text-align:center">
<a href="https://github.com/kingFighter"                   target="_blank">
<i class="fa fa-github" style="text-align:center"></i></a>
<a href="mailto:kevinlui598@gmail.com" target="_blank">
<i class="mdi-communication-email" style="text-align:center"></i></a>
</h3>
"""
