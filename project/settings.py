import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'adminsortable2',
    'ckeditor',
    'ckeditor_uploader',
    'base.apps.CustomConstance',
    'constance.backends.database',
    'imagekit',

    'base.apps.BaseConfig',
    'callback.apps.CallbackConfig',
    'blog.apps.BlogConfig',
    'gallery.apps.GalleryConfig',
    'socials.apps.SocialsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'base.context_processors.photo_categories',
                'base.context_processors.callback',
                'base.context_processors.social_icons',
                'constance.context_processors.config',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = "uploads/"

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [['Source', '-', 'Save', 'NewPage', 'Preview', '-'],
                    ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
                    ['Find', 'Replace', '-', 'SelectAll', '-'],
                    ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting',
                     'RemoveFormat'],
                    ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                     'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-'],
                    ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
                    ['Link', 'Unlink', 'Anchor'],
                    ['Styles', 'Format', 'Font', 'FontSize'], ['TextColor', 'BGColor'], ['Maximize', 'ShowBlocks'],
                    ],
        'height': 600,
        'width': 1000
        # 'toolbar': None,
        # 'enterMode': 2,
        # 'shiftEnterMode': 3
    },

}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

CONSTANCE_CONFIG = {
    'PHONE': ('+7 (495) 150-66-68', ''),
    'PHONE_2': ('8 (926) 22-66-844', ''),
    'EMAIL': ('maximokna@list.ru', ''),
    'ADDRESS': ('127566 г. Москва, Алтуфьевское ш, д. 48, корпус 2', ''),
    'WORK_HOURS': ('9<sub class="work-hours__number_sub">:00</sub>'
                   ' - 21<sub class="work-hours__number_sub">:00</sub>', ' '),
    'COPYRIGHT': ('© 2019 MAXIMOKNA', ' '),
    'PRODUCT_MENU': ('<ul class="product-list"><li class="product__item"><a class="product__link" href="/plastikovye-okna/">Пластиковые окна</a></li><li class="product__item"><a class="product__link" href="">Остекление балконов и лоджий</a></li><li class="product__item"><a class="product__link" href="">Остекление квартир</a></li><li class="product__item"><a class="product__link" href="">Балконные двери</a></li><li class="product__item"><a class="product__link" href="">Энергосберегающие окна</a></li></ul><ul class="product-list"><li class="product__item"><a class="product__link" href="">Остекление загородного дома</a></li><li class="product__item"><a class="product__link" href="">Раздвижные двери и окна</a></li><li class="product__item"><a class="product__link" href="">Остекление беседок и веранд</a></li><li class="product__item"><a class="product__link" href="">Панорамные окна</a></li><li class="product__item"><a class="product__link" href="">Входные двери и группы</a></li></ul><ul class="product-list"><li class="product__item"><a class="product__link" href="">Фасадное остекление</a></li><li class="product__item"><a class="product__link" href="">Аллюминиевые окна</a></li><li class="product__item"><a class="product__link" href="">Рулонные шторы и жалюзи</a></li><li class="product__item"><a class="product__link" href="">Рольставни</a></li></ul>', ' '),
    'SERVICE_MENU': ('<ul class="service-list"><li class="service__item"><a class="service__link" href="">Замер</a></li><li class="service__item"><a class="service__link" href="">Доставка</a></li><li class="service__item"><a class="service__link" href="">Монтаж</a></li><li class="service__item"><a class="service__link" href="">Сервис</a></li><li class="service__item"><a class="service__link" href="">Ремонт</a></li></ul>', '')
}
