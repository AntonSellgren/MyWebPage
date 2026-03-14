from flask import Flask
from webserver.config import Config
from dotenv import load_dotenv
import os

# Create flask app
app = Flask(__name__)

# Load config class
app.config.from_object(Config)

# Load environment variables from .env file
load_dotenv(os.getcwd() + "/.env")

# Access environment variables and setting app config
app.config["DATABASE_URL"] = os.getenv("DATABASE_URL")
app.config["DATABASE_USER"] = os.getenv("DATABASE_USER")
app.config["DATABASE_PASSWORD"] = os.getenv("DATABASE_PASSWORD")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SECURITY_PASSWORD_SALT"] = os.getenv("SECURITY_PASSWORD_SALT")

# Starts routing
from webserver import routes
