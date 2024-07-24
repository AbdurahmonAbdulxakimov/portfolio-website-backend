from .base import *  # noqa

DEBUG = True
CELERY_TASK_ALWAYS_EAGER = True
CSRF_TRUSTED_ORIGINS = [env.str('BACKEND_HOST_URL')]