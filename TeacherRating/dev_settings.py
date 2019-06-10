from TeacherRating.common_settings import *

DEBUG = True
SECRET_KEY = 'rlc(9$ia0y71pe&12zh5!0ela2nm63w=lzk5o6218be3p3u_8@'
INSTALLED_APPS += [
	'debug_toolbar',
]

DATABASE['default'].update({
	'NAME': 'TeacherRating',
    'USER': 'postgres',
    'PASSWORD': 'pass',
    'HOST': '127.0.0.1',
    'PORT': '5432'
})

CACHES = {'default': {
	'BACKEND':'django.teacher_rating.cache.backends.locmem.LocMemCache',
	'LOCATION':'default-locmemcache',
	'TIMEOUT':6
	}
}

MEDIA_ROOT = os.path.join(BASE_DIR,'../media_root')

INTERNAL_IPS = ('127.0.0.1',)
