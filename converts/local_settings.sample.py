# Create a file local_settings.py using this as a template
from datetime import date

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/path/to/the/db/file/converts.sqlite3',
    }
}

# The start date of your first period
START_DATE = date(2014, 4, 10)

# It is reasonable to choose the period length so that
# it matches the periodicity of your main income
PERIOD_LENGTH = 'f'