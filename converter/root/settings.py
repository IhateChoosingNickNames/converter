import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv(
    "SECRET_KEY",
    default="django-insecure-&*0d2s9fk(6f3^cr6r1$fl5-^vm7*m)ry5i+b0v3%&2z#%@w#b",
)


DEBUG = False

ALLOWED_HOSTS = (
    os.getenv("CONTAINER_NAME"),
)
INTERNAL_IPS = (
    os.getenv("LOCALHOST_IP"),
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Сторонние либы
    "rest_framework",

    # Приложения
    "api.apps.ApiConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "root.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "root.wsgi.application"


# Sqlite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


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


LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = False

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon": "120/min",
    },
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
}

EXCHANGE_ENDPOINT = "http://api.exchangeratesapi.io/v1/latest"
REQUEST_TIMEOUT = 10  # секунд
API_KEY = os.getenv("API_KEY")