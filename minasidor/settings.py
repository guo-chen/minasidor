"""
Django settings for minasidor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in producti on secret!
SECRET_KEY = 'k@)#n(hz!w@*r$7(d^8&)cj)m8&$r73fc#6v=j-tg5e@)-vb5s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'minasidor.urls'

WSGI_APPLICATION = 'minasidor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'blog/static/'),
)

# Template directories

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


# CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = 'http://code.jquery.com/jquery-latest.min.js'
# CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
    'basic': {
        'toolbar': 'Basic',
    },
    'customized': {
        'toolbar': [["Source"],
                    ["Format", "Font", "Bold", "Italic", "Underline", "Strike", "TextColor", "Subscript", "Superscript", "RemoveFormat"],
                    ['Undo', 'Redo'],
                    ["Scayt", "Save"],
                    ['NumberedList', 'BulletedList'],
                    ["Indent", "Outdent", 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                    ["Link", "Unlink", "Anchor"],
                    ["CodeSnippet", "texzilla", "Smiley", "Blockquote", "Image", "Table"],
                    ["Maximize"],
                    ],
        'extraPlugins': "codesnippet,texzilla",
        'codeSnippet_theme': "github",
        'codeSnippet_languages': {'bash': "Bash",
                                  'python': "Python",
                                  'perl': "Perl",
                                  'html': "HTML",
                                  'makefile': "Makefile",
                                  'nginx': "Nginx",
                                  'cpp': "C++",
                                  },
    },
}

# Media
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

