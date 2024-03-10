from os import environ as env
from dotenv import load_dotenv
load_dotenv()

TOKEN = env['TOKEN']
RANGO_API_KEY = env['RANGO_API_KEY']
RANGO_BASE_URL = env['RANGO_BASE_URL']
WEBHOOK_URL = env['WEBHOOK_URL']