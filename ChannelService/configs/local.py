from pathlib import Path, PurePath

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7#k(1x7au-q-2uq1_73tt9fbe3c5g8!kaa*fwmu_%*b+1wfj#t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.ngrok.io',
    '.127.0.0.1',
    '.localhost',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    Path(PurePath(BASE_DIR, 'static')),
]
