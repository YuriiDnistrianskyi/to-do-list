from os import getenv
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = getenv("DATABASE_URL")
SECRET_JWT_KEY = getenv("SECRET_JWT_KEY")

SMTP_HOST = getenv("SMTP_HOST")
SMTP_PORT = getenv("SMTP_PORT")
SMTP_USERNAME = getenv("SMTP_USERNAME")
SMTP_PASSWORD = getenv("SMTP_PASSWORD")
SMTP_FROM = getenv("SMTP_FROM")
