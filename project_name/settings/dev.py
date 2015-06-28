from .base import *

DEBUG = True

try:
    from .local import *
except ImportError:
    pass


import datetime
JWT_AUTH = {
    'JWT_SECRET_KEY': '{{ project_name }}',
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3000),
    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}