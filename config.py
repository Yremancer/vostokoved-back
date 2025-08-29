from dotenv import load_dotenv
import os

load_dotenv()

 
WEB_URL = os.getenv('WEB_URL')

ORIGINS = [WEB_URL]

