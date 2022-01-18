import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = config('APP_NAME', default='Super Mini Divar')
APP_DESCRIPTION = config('APP_DESCRIPTION', default='A simple Backend for Ads And Requirements System Like Divar')
APP_VERSION = config('APP_VERSION', default='0.1.0')
APP_HOST = config('APP_HOST', default='127.0.0.1')
APP_PORT = config('APP_PORT', default=5000, cast=int)
DEBUG = config('DEBUG', default=True, cast=bool)
DB_URI = config('DB_URI')
JWT_SECRET_KEY = config('JWT_SECRET_KEY')
