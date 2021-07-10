from .settings import *

DEBUG = bool(int(os.environ.get("DEBUG", default=1)))

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': 'db.sqlite3',
   }
}
