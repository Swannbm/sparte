"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
hello world
"""
import environ
from pathlib import Path
import pkg_resources

from django.core.exceptions import ImproperlyConfigured


root = environ.Path(__file__) - 2  # get root of the project
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(root())

# initialize env with environment variable
# it can contains DEBUG (in production env it shall)
# so we could explore how to load file only on local execution
env = environ.Env()

env_path = BASE_DIR / ".env"
if env_path.is_file():
    environ.Env.read_env(str(env_path))  # reading .env file

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
]

RESTFRAMEWORK_APPS = [
    "rest_framework",
    "rest_framework_gis",
]

THIRD_APPS = [
    "import_export",
    "crispy_forms",
]

# upper app should not communicate with lower ones
PROJECT_APPS = [
    "app_parameter.apps.AppParameterConfig",
    "users.apps.UsersConfig",
    "carto.apps.CartoConfig",
    "public_data.apps.PublicDataConfig",
    "project.apps.ProjectConfig",
    "home.apps.HomeConfig",
]

INSTALLED_APPS = DJANGO_APPS + RESTFRAMEWORK_APPS + THIRD_APPS + PROJECT_APPS


MIDDLEWARE = [
    "config.middlewares.LogIncomingRequest",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "users.context_processors.add_connected_user_to_context",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# require DATABASE_URL in .env file
DATABASES = {
    "default": env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# indicate the new User model to Django
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "carto:home_connected"
LOGIN_URL = "users:signin"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = str(BASE_DIR / "staticroot")

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# same goes for media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Bucket S3 and filestorage
# see https://django-storages.readthedocs.io/en/latest/

# specify to django we use only S3 to store files
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# credentials
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

# bucket name and region
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")

# append a prefix to all uploaded file (useful to not mix local, staging...)
AWS_LOCATION = env("AWS_LOCATION")
# avoid overriding a file if same key is provided
AWS_S3_FILE_OVERWRITE = False
# allow signed url to be accessed from all regions
AWS_S3_SIGNATURE_VERSION = "s3v4"


# django-import-export
# https://django-import-export.readthedocs.io/en/latest/
IMPORT_EXPORT_USE_TRANSACTIONS = True


# Crispy configuration
# https://django-crispy-forms.readthedocs.io/en/latest/index.html
# set default rendering
CRISPY_TEMPLATE_PACK = "bootstrap4"


# Celery configuration
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_ACKS_LATE = True

# django-debug-toolbar configuration

# activate only if debug is True
# and only if package is available
if DEBUG:
    try:
        # only if debug_toolbar is available, else it will fire exception
        # useful to turn debug mode on staging without installing dev dependencies
        import debug_toolbar  # noqa: F401

        INSTALLED_APPS += ["debug_toolbar"]
        MIDDLEWARE += [
            "debug_toolbar.middleware.DebugToolbarMiddleware",
        ]

        # bypass check of internal IPs
        def show_toolbar(request):
            return True

        DEBUG_TOOLBAR_CONFIG = {
            "SHOW_TOOLBAR_CALLBACK": show_toolbar,
        }

    except ImportError:
        pass


# EMAIL
"""Configuration of e-mails

Several configuration are authorized, see available_engines variable below.

Local = will store email to a file (not sending)
mailjet = will use mailjet provider to send emails, it uses anymail lib, see
https://anymail.readthedocs.io/en/stable/esps/mailjet/

To set local configuration, please add to .env file following variables:
- EMAIL_ENGINE=local
- EMAIL_FILE_PATH where to store a file for each sent email

To set MailJet configuration, please add environment variables:
- EMAIL_ENGINE=mailjet
- MAILJET_ID & MAILJET_SECRET, see https://app.mailjet.com/account/api_keys
"""

EMAIL_ENGINE = env("EMAIL_ENGINE")

available_engines = ["local", "mailjet"]
if EMAIL_ENGINE not in available_engines:
    raise ImproperlyConfigured("E-mail backend needs to be correctly set")


if EMAIL_ENGINE == "local":
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = env.str("EMAIL_FILE_PATH")

elif EMAIL_ENGINE == "mailjet":
    INSTALLED_APPS += [
        "anymail",
    ]
    EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
    ANYMAIL = {
        "MAILJET_API_KEY": env("MAILJET_ID"),
        "MAILJET_SECRET_KEY": env("MAILJET_SECRET"),
    }

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# used by ./manage.py shell_plus --notebook
if "django-extensions" in {pkg.key for pkg in pkg_resources.working_set}:
    INSTALLED_APPS += [
        "django_extensions",
    ]
    NOTEBOOK_ARGUMENTS = [
        "--ip",
        "0.0.0.0",
        "--allow-root",
        '--notebook-dir="/app/notebooks/"',
    ]

# RESTRAMEWORK parameters
# https://www.django-rest-framework.org

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination"
}

# LOGGING SETTINGS

LOGGING_LEVEL = env.str("LOGGING_LEVEL", default="INFO")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "just_message": {
            "format": "[{asctime}] {message}",
            "style": "{",
            "datefmt": "%Y/%b/%d %H:%M:%S",
        },
        "verbose": {
            "format": "[{asctime}]{levelname:<7} {module} {process:d} {thread:d} {message}",
            "style": "{",
            "datefmt": "%Y/%b/%d %H:%M:%S",
        },
        "simple": {
            "format": "[{asctime}]{levelname:<7} {message}",
            "style": "{",
            "datefmt": "%Y/%b/%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "console_just_message": {
            "class": "logging.StreamHandler",
            "formatter": "just_message",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "config": {
            "handlers": ["console_just_message"],
            "level": LOGGING_LEVEL,
            "propagate": False,
        },
    },
}
