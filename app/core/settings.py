from datetime import date, datetime

from decouple import config

DB_SERVER = config('DB_SERVER', default='localhost')
DB_DATABASE = config('DB_DATABASE')
DB_SCHEMA = config('DB_SCHEMA', default='dbo')
DB_USERNAME = config('DB_USERNAME')
DB_PASSWORD = config('DB_PASSWORD')
DB_DRIVER = 'ODBC+Driver+17+for+SQL+Server'

DB_CONNECTION_STRING = f'mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_DATABASE}?driver={DB_DRIVER}'

# Sage X3 database table settings
DEFAULT_LEGACY_DATE = date(1753, 1, 1)
DEFAULT_LEGACY_DATETIME = datetime(1753, 1, 1)
