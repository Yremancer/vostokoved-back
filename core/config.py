from dotenv import load_dotenv
import os

load_dotenv()

 
WEB_URL = os.getenv('WEB_URL')

ORIGINS = [WEB_URL]

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')

LLM_ON = True if os.getenv('LLM_ON') == "True" else False

