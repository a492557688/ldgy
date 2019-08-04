"""
Django settings for Myproject project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys

sys.path.append(os.path.dirname(BASE_DIR))
sys.path.append(os.path.join(BASE_DIR,"apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g+-+dt(pz6uz0yxtf-33sf)#0mllc6ev%)2s3-=n_m7z=zkn=@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "home",
    "rest_framework",
    'xadmin',
    # 渲染表格模块
    'crispy_forms',
    "django_filters",
    # 为模型通过版本控制，可以回滚数据
    'reversion',
    "Myproject",
    "corsheaders",
    "filter",
    "detail",
    "process_from",

]
SITE_ID = 1
AUTH_USER_MODEL ="home.MyUser"
MIDDLEWARE = [
    # "django.middleware.cache.UpdateCacheMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'django.middleware.cache.FetchFromCacheMiddleware', #最后
    'corsheaders.middleware.CorsMiddleware',
    "Myproject.utils.my_middleware.Redis_middleware",
    "Myproject.utils.my_middleware.Cors_middleware"
]
CACHE_MIDDLEWARE_SECONDS=60*60*3
ROOT_URLCONF = 'Myproject.urls'
CORS_ORIGIN_ALLOW_ALL = True





TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../../logs/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "ldgy4",
        "USER":"root",
        "PASSWORD":"123",
        "HOST":"127.0.0.1",
        "PORT":3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
CACHES = {
"default": {
"BACKEND": "django_redis.cache.RedisCache",
"LOCATION": "redis://127.0.0.1:6379",
"OPTIONS": {
"CLIENT_CLASS": "django_redis.client.DefaultClient",
"CONNECTION_POOL_KWARGS": {"max_connections": 100}
}
}
    }

EMAIL_HOST = 'smtp.qq.com'  # 如果是 163 改成 smtp.163.com
EMAIL_PORT = 465
EMAIL_HOST_USER = '492557688@qq.com'  # 发送邮件的邮箱帐号
EMAIL_HOST_PASSWORD = 'ridwinqkhnrpbijj'  # 授权码,各邮箱的设置中启用smtp服务时获取
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_SSL = True

# CACHES = {
#  'default': {
#   'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache', #指定缓存使用的引擎
#   'LOCATION': 'c/django_cache',        #指定缓存的路径
#   'TIMEOUT':30,              # 为什么只有10秒  /300/30
#   'OPTIONS':{
#    'MAX_ENTRIES': 300,            # 最大缓存记录的数量（默认300）
#    'CULL_FREQUENCY': 3,           # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
#   }
#  }
# }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")]
MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, "media")