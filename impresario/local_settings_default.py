
# SECURITY WARNING: keep the secret key used in production secret!
# Sample python code:
# from django.utils.crypto import get_random_string
# chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
# get_random_string(50, chars)
SECRET_KEY = 'n$44_x+23^epe4%6+f)gch=#&x)5k0obt_e_hpp3s651s5dzsq'

ALLOWED_HOSTS = []
INTERNAL_IPS = ['127.0.0.1']

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATIC_URL = '/static/'
