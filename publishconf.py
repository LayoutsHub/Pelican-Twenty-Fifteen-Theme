# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://layoutshub.github.io/pelican-twenty-fifteen-theme"
RELATIVE_URLS = False

#FEED_ALL_ATOM = "feeds/all.atom.xml"
#CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Disqus Comment Plugin
DISQUS_USERNAME = None

# Google Analytics Tracking
GOOGLE_ANALYTICS_ID = None