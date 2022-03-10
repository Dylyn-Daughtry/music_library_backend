# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c(3p%3jm2_fdg@kp^qy@pqa&n01tx*26zs8tzcl+@7w)hc7t!5'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_database',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'Daughtry',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
