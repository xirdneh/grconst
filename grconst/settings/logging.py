import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.join(PROJECT_DIR, '..')


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters':{
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'log_error': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/var/log/grconst/grconst.error.log',
            'when': 'D',
            'encoding': 'utf-8',
            'formatter': 'verbose',
            'backupCount': 0 
        },
        'log_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/var/log/grconst/grconst.debug.log',
            'when': 'D',
            'encoding': 'utf-8',
            'formatter': 'verbose',
            'backupCount': 0
        }
    },
    'loggers': {
        'grconst':{
            'handlers':['log_debug'],
            'level':'DEBUG',
            'propagate':True,
        },
        'django':{
            'handlers':['log_debug'],
            'level':'DEBUG',
            'propagate':True,
        },
    }
}
