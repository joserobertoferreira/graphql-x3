from datetime import date, datetime

from decouple import config

DB_SERVER = config('DB_SERVER', default='localhost')
DB_DATABASE = config('DB_DATABASE')
DB_SCHEMA = config('DB_SCHEMA', default='dbo')
DB_USERNAME = config('DB_USERNAME')
DB_PASSWORD = config('DB_PASSWORD')
DB_DRIVER = 'ODBC+Driver+17+for+SQL+Server'

DB_CONNECTION_STRING = f'mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_DATABASE}?driver={DB_DRIVER}'

# Authentication settings
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM', default='HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = config('ACCESS_TOKEN_EXPIRE_MINUTES', default=30, cast=int)

# Sage X3 database table settings
DEFAULT_LEGACY_DATE = date(1753, 1, 1)
DEFAULT_LEGACY_DATETIME = datetime(1753, 1, 1)

# Constants for Sage X3 database tables
LITERAL_ZERO = 0
LITERAL_ONE = 1
LITERAL_TWO = 2
LITERAL_THREE = 3
LITERAL_FOUR = 4
LITERAL_FIVE = 5
LITERAL_SIX = 6
LITERAL_SEVEN = 7
LITERAL_EIGHT = 8
LITERAL_NINE = 9
LITERAL_TEN = 10

# Password validation parameters
PASSWORD_MIN_LENGTH = config('PASSWORD_MIN_LENGTH', default=8, cast=int)
PASSWORD_MAX_LENGTH = config('PASSWORD_MAX_LENGTH', default=20, cast=int)

# Username validation parameters
USERNAME_MIN_LENGTH = config('USERNAME_MIN_LENGTH', default=4, cast=int)
USERNAME_MAX_LENGTH = config('USERNAME_MAX_LENGTH', default=15, cast=int)
