from os import getenv
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = getenv("DATABASE_URL")
SECRET_JWT_KEY = getenv("SECRET_JWT_KEY")
