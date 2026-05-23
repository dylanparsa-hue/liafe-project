import os
import dj_database_url
from pathlib import Path
from django.urls import reverse_lazy
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-liafe-dev-key-change-in-production-xyz123')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost 127.0.0.1').split()

CSRF_TRUSTED_ORIGINS = [
    'https://*.trycloudflare.com',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
] + [
    origin for origin in os.environ.get('CSRF_TRUSTED_ORIGINS', '').split()
    if origin
]

INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'unfold.contrib.inlines',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cloudinary',
    'cloudinary_storage',
    'ckeditor',
    'ckeditor_uploader',

    'core',
    'services',
    'publications',
    'messages_app',
    'dashboard',
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'liafe_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.site_settings',
                'dashboard.context_processors.dashboard_counts',
            ],
        },
    },
]

WSGI_APPLICATION = 'liafe_project.wsgi.application'

# Database — Railway sets DATABASE_URL automatically when you add PostgreSQL.
# Locally falls back to SQLite.
_db_url = os.environ.get('DATABASE_URL')
if _db_url:
    DATABASES = {'default': dj_database_url.config(default=_db_url, conn_max_age=600, ssl_require=True)}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ── Cloudinary (production media storage) ────────────────────────────────────
# In Railway, set CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET.
# Locally, files are stored in the media/ folder as normal.
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME', ''),
    'API_KEY':    os.environ.get('CLOUDINARY_API_KEY', ''),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET', ''),
}
if os.environ.get('CLOUDINARY_CLOUD_NAME'):
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ── Production security ───────────────────────────────────────────────────────
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE   = True
    CSRF_COOKIE_SECURE      = True
    SECURE_BROWSER_XSS_FILTER      = True
    SECURE_CONTENT_TYPE_NOSNIFF    = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/dashboard/'

# CKEditor
CKEDITOR_UPLOAD_PATH = 'ckeditor_uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike'],
            ['NumberedList', 'BulletedList', '-', 'Blockquote'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
        ],
        'height': 300,
        'width': '100%',
    },
}

# ── Django Unfold Admin Theme ────────────────────────────────────────────────
UNFOLD = {
    "SITE_TITLE": "LIAFE CMS",
    "SITE_HEADER": "LIAFE",
    "SITE_URL": "/",
    "SITE_ICON": None,
    "SITE_SYMBOL": "language",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "DASHBOARD_CALLBACK": "core.admin.dashboard_callback",

    "STYLES": [
        lambda request: "/static/css/admin.css",
    ],
    "SCRIPTS": [],

    "COLORS": {
        "base": {
            "50":  "249 250 251",
            "100": "243 244 246",
            "200": "229 231 235",
            "300": "209 213 219",
            "400": "156 163 175",
            "500": "107 114 128",
            "600": "75  85  99",
            "700": "55  65  81",
            "800": "31  41  55",
            "900": "17  24  39",
            "950": "3   7   18",
        },
        "primary": {
            "50":  "255 251 235",
            "100": "254 243 199",
            "200": "253 230 138",
            "300": "252 211 77",
            "400": "251 191 36",
            "500": "201 162 39",
            "600": "168 138 44",
            "700": "126 102 32",
            "800": "92  73  23",
            "900": "69  52  22",
            "950": "45  33  14",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",
            "subtle-dark": "var(--color-base-400)",
            "default-light": "var(--color-base-700)",
            "default-dark": "var(--color-base-200)",
            "important-light": "var(--color-base-900)",
            "important-dark": "var(--color-base-100)",
        },
    },

    "TABS": [],

    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": False,
        "navigation": [
            {
                "title": "Dashboard",
                "separator": False,
                "items": [
                    {
                        "title": "Overview",
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": "View Website",
                        "icon": "open_in_new",
                        "link": "/",
                        "target": "_blank",
                    },
                ],
            },
            {
                "title": "Website Settings",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Site Settings",
                        "icon": "tune",
                        "link": reverse_lazy("admin:core_sitesetting_changelist"),
                    },
                    {
                        "title": "Value Pillars",
                        "icon": "stars",
                        "link": reverse_lazy("admin:core_valuepillar_changelist"),
                    },
                    {
                        "title": "Contact Page",
                        "icon": "contact_page",
                        "link": reverse_lazy("admin:messages_app_contactpage_changelist"),
                    },
                ],
            },
            {
                "title": "Homepage",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Hero Slides",
                        "icon": "slideshow",
                        "link": reverse_lazy("admin:core_heroslide_changelist"),
                    },
                    {
                        "title": "Homepage Sections",
                        "icon": "home",
                        "link": reverse_lazy("admin:core_homepagesection_changelist"),
                    },
                ],
            },
            {
                "title": "Services",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "All Services",
                        "icon": "grid_view",
                        "link": reverse_lazy("admin:services_service_changelist"),
                    },
                    {
                        "title": "Service Features",
                        "icon": "featured_play_list",
                        "link": reverse_lazy("admin:services_servicefeature_changelist"),
                    },
                ],
            },
            {
                "title": "Academy",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Course Categories",
                        "icon": "school",
                        "link": reverse_lazy("admin:services_coursecategory_changelist"),
                    },
                    {
                        "title": "Courses",
                        "icon": "menu_book",
                        "link": reverse_lazy("admin:services_course_changelist"),
                    },
                ],
            },
            {
                "title": "Research House",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Research Categories",
                        "icon": "science",
                        "link": reverse_lazy("admin:services_researchcategory_changelist"),
                    },
                    {
                        "title": "Research Projects",
                        "icon": "biotech",
                        "link": reverse_lazy("admin:services_researchproject_changelist"),
                    },
                ],
            },
            {
                "title": "Publications",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "All Publications",
                        "icon": "auto_stories",
                        "link": reverse_lazy("admin:publications_publication_changelist"),
                    },
                    {
                        "title": "Add Publication",
                        "icon": "add_circle",
                        "link": reverse_lazy("admin:publications_publication_add"),
                    },
                ],
            },
            {
                "title": "Messages",
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": "Contact Messages",
                        "icon": "mail",
                        "link": reverse_lazy("admin:messages_app_contactmessage_changelist"),
                    },
                    {
                        "title": "Inquiries",
                        "icon": "help",
                        "link": reverse_lazy("admin:messages_app_inquiry_changelist"),
                    },
                ],
            },
            {
                "title": "Users & Access",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Users",
                        "icon": "person",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": "Groups",
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}
