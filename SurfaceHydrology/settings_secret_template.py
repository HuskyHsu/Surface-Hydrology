SECRET_KEY = 'YOUR-SECRET_KEY'

DATABASES = {
    'default': {
        'ENGINE': 'YOUR_DB_ENGINE',             # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'YOUR_DB_NAME',                 # Or path to database file if using sqlite3.
        'USER': 'YOUR_DB_USERNAME',             # Not used with sqlite3.
        'PASSWORD': 'YOUR_DB_PASSWORD',         # Not used with sqlite3.
        'HOST': 'YOUR_DB_IP',                   # Set to empty string for localhost. Not used with sqlite3.
        'PORT': 'YOUR_DB_PORT',                 # Set to empty string for default. Not used with sqlite3.
    }
}


import asyncio
from aiomysql import create_pool

def create_aiomysql(loop):
    
    return create_pool(
        host = 'YOUR_DB_IP',
        user = 'YOUR_DB_USERNAME',
        password = 'YOUR_DB_PASSWORD',
        db = 'YOUR_DB_NAME',
        loop = loop)