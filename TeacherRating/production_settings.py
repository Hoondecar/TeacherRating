from TeacherRating.common_settings import *

DEBUG = False

assert SECRET_KEY is not None,(
	'Please provide DJANGO_SECRET_KEY'
	'SOSI HUI')
ALLOWED_HOSTS += [
	os.getenv('DJANGO_ALLOWED_HOSTS')
]