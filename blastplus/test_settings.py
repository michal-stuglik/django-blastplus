from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'abc'
    }
}

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django_nose',
    'coverage',
    'blastplus',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'blastplus.urls'

TEMPLATE_DIRS = [
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "blastplus/templates"),
]

STATIC_URL = '/static/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'set-secret-key-here'  # set-secret-key-here

# # testing suit
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=blastplus',
    '--cover-inclusive',
    '--verbosity=2',
]
