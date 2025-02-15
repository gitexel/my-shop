"""
Django settings for my_shop project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^muzt342(d0_ktu884@4xa#63q6pu9xb70*097xjjqnm1^1(4%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "erp_framework",
    "sales",
    "expense",
    "general_reports",
    "purchase",
    "crequest",
    "crispy_forms",
    "crispy_bootstrap4",
    "reversion",
    "tabular_permissions",
    "erp_framework.admin.jazzmin_integration",
    "erp_framework.admin",
    "erp_framework.activity",
    "erp_framework.reporting",
    "slick_reporting",
    "jazzmin",
    "django.contrib.admin",  # comes at the end because the theme is replaced
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # crequest
    "crequest.middleware.CrequestMiddleware",
]

ROOT_URLCONF = "my_shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],  # add this line
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

WSGI_APPLICATION = "my_shop.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_TEMPLATE_PACK = "bootstrap4"

STATIC_ROOT = BASE_DIR / "collected_static"

SLICK_REPORTING_FORM_MEDIA = {}

SLICK_REPORTING_DEFAULT_CHARTS_ENGINE = "highcharts"

# RA_ADMIN_INDEX_PAGE = "admin/custom_index.html"
# RA_ADMIN_INDEX_TITLE = "My Shop"
JAZZMIN_SETTINGS = {
    "site_brand": "My Shop ERP System",
    "welcome_sign": "Welcome to Django ERP framework demo site. \n Use Username:`test` Password:`testuser123` to login",
}

ERP_FRAMEWORK_SETTINGS = {
    "index_title": "My Shop dashboard",
    "index_template": "admin/custom_index.html",
}

LOGIN_REDIRECT_URL = reverse_lazy("admin:index", current_app="erp_framework_admin")
