from dotenv import load_dotenv
import os


load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
SMTP_PASS = os.environ.get("SMTP_PASS")
SMTP_USER = os.environ.get("SMTP_USER")
