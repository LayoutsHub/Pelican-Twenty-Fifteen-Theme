AUTHOR = 'Layouts Hub'
SITENAME = "Layout Hub"
SITEURL = "https://layoutshub.github.io/pelican-twenty-fifteen-theme"
SITE_LOGO_URL = "YOUR_SITE_LOGO"
SITE_SUMMARY = "A collection of Pelican, Jekyll, Hugo, Gatsby theme. Ported themes from other cms."

PATH = "content"
PAGE_PATHS = ['pages']
OUTPUT_PATH = 'docs/'

THEME = "themes/twenteenFifteen"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'uncategorized'

# Disqus Comment Plugin
DISQUS_USERNAME = None

# Google Analytics Tracking
GOOGLE_ANALYTICS_ID = None

# Social Username
# Needed for Author Schema. You can modify author schema in includes/authorSchema.html
FACEBOOK_USERNAME = "YOUR_FACEBOOK_USERNAME"
TWITTER_USERNAME = "YOUR_TWITTER_USERNAME"
LINKEDIN_USERNAME = "YOUR_LINKEDIN_USERNAME"

# URL Structure
ARTICLE_URL = "{slug}.html"

# Static Page
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Ignore
IGNORE_FILES = ['404.html']

# Disable unwanted pages
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Cache
GZIP_CACHE = True

# Pagination
# Enable pagination with the desired pattern
DEFAULT_PAGINATION = 2  # This should show 2 articles per page
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}.html', '{base_name}/page/{number}.html'),
)

# Plugins
SITEMAP = {
    "exclude": [
        "^/noindex/",  # starts with "/noindex/"
        "category/",
        "404.html",
        "index.*.html",
        "page.*.html",
        "\.json$"   # ends with ".json"
    ]
}

PLUGINS = ['minify','sitemap']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS =  True