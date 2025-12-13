from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES = {
    'NAME': os.getenv('POSTGRES_DB'),
    'USER': os.getenv('POSTGRES_USER'),
    'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
    'HOST': os.getenv('POSTGRES_HOST'),
    'PORT': os.getenv('POSTGRES_PORT'),
}

API_SERVICE_URL = os.getenv('API_SERVICE_URL')
MODEL_UPDATE_SECRET = os.getenv('MODEL_UPDATE_SECRET')