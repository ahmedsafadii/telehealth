import environ

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, [])
)
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

DEBUG = bool(env('DEBUG')) # Make true in production mode

SALT = env('SALT')


SECURE_HSTS_SECONDS = 60

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SESSION_COOKIE_SECURE = True

# SECURE_SSL_REDIRECT = True # Enable this in production mode

CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db(),
}
