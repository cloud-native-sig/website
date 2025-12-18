AUTHOR = 'Cloud Native SIG'
SITENAME = 'Cloud Native SIG'
SITESUBTITLE = 'A Community for Cloud-Native Technologies in Digital Research'
DESCRIPTION = 'A Community for Cloud-Native Technologies in Digital Research'
SITEURL = '' # Overriden by publishconf.py
SITEIMAGE = '/images/cloud-native-sig-logo.png'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

# Theming
STATIC_PATHS = ['extra', 'images']
EXTRA_PATH_METADATA = {
    'extra/css/flatly.min.css': {'path': 'theme/css/flatly.min.css'},
    'extra/css/custom.css': {'path': 'theme/css/custom.css'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'images/cloud-native-sig-logo.png': {'path': 'images/cloud-native-sig-logo.png'},
}
THEME = 'themes/pelican-alchemy/alchemy'
THEME_TEMPLATES_OVERRIDES = ['themes/custom-alchemy/templates'] # Includes customer footer override
THEME_CSS_OVERRIDES = ['theme/css/custom.css'] # Centre images!
BOOTSTRAP_CSS = '/theme/css/flatly.min.css' # Bootswatch theme
PYGMENTS_STYLE = 'monokai' # Code syntax style
RFG_FAVICONS = True # Uses favicon/icons defined in EXTRA_PATH_METADATA

# Keep author name on articles
HIDE_AUTHORS = False
# Top-level directory for written site content
PATH = "content"
# Display pages in header (e.g. about page)
DISPLAY_PAGES_ON_MENU = True
# Subdirectory for articles
ARTICLE_PATHS = ['articles']
# Links in header
LINKS = (
    ('Kubernetes Tutorial', "https://rosalindfranklininstitute.github.io/rsecon25-intro-to-kubernetes/"),
    ("Mailing List", "https://www.jiscmail.ac.uk/cgi-bin/wa-jisc.exe?SUBED1=CLOUDNATIVE-SIG"),
)
# Social icons in header
ICONS = (
    ('github', 'https://github.com/cloud-native-sig'),
    ('fas fa-envelope', '#'), # Set a mailto: address?
)
# Links in footer
FOOTER_LINKS = (
    ('About', '/pages/about.html'),
    ('Events', '/category/events.html'),
    ('Tags', '/tags.html') # consider categories instead
)

# Feed generation (disabled)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Number of articles before paginate
DEFAULT_PAGINATION = 10
