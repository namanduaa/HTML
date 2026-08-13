# django_project_example.py
# A simple Django project example showing the core setup.

from django.conf import settings
from django.http import HttpResponse
from django.urls import path


# 1. Configure project settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='my-secret-key',
    ALLOWED_HOSTS=['*'],
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
    ROOT_URLCONF=__name__,
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    STATIC_URL='/static/',
)


# 2. View function

def home(request):
    return HttpResponse("<h1>Welcome to my Django project!</h1>")


# 3. URL patterns
urlpatterns = [
    path('', home, name='home'),
]


# 4. Example startup block
if __name__ == '__main__':
    import django

    django.setup()
    print('Django project is configured successfully.')
    print('Run: python manage.py runserver')
    print('Open: http://127.0.0.1:8000/')
