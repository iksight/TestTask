import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = os.getenv('DEBUG', True)

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't)2z-(h0pw+pok2f9#vn$h0$v8od)0n-3)hxpnw!kf$#zfuxum'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
