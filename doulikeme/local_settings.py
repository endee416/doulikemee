import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'questions',
        'USER':'postgres',
        'PASSWORD': '12345',
        'HOST':'localhost',
        'PORT':'5432'
    }
}