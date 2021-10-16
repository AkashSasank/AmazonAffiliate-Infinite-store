import os
from dotenv import load_dotenv
from .settings import MIDDLEWARE

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware'
                  )
