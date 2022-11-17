from .settings import *

DEBUG = True
SECRET_KEY = 'jkus32q*$0b^0^2na!#f_9si@oibsg9ogvehh)g48@_7ycv80$'
ALLOWED_HOSTS = ['127.0.0.1']
DATABASES = {
    'dafault': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}