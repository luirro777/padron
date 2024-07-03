from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["padron.local.com","localhost","127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

RECAPTCHA_PUBLIC_KEY = get_secret('R_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = get_secret('R_PRIVATE_KEY')

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
DATA_UPLOAD_MAX_NUMBER_FIELDS = 25000

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# EMAIL SETTINGS
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = get_secret('EMAIL')
#EMAIL_HOST_PASSWORD = get_secret('PASS_EMAIL')
#EMAIL_PORT = 587