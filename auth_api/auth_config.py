from flask import Blueprint, render_template, request
from flask.json import jsonify

from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy, inspect
"""
Основной модуль
"""
import logging
import os
import shutil
import sys
import time
from flask import Flask

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://postgres:123@127.0.0.1:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    # JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    # JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    # ACCESS_EXPIRES = timedelta(hours=1)
    SWAGGER_TEMPLATE = {
        "securityDefinitions": {
            "APIKeyHeader": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token",
            }
        }
    }
    # MIGRATIONS_PATH = os.getenv("MIGRATIONS_PATH")

db = SQLAlchemy(session_options={"autoflush": False})
migrate_obj = Migrate()
# engine = db.create_engine(Config.SQLALCHEMY_DATABASE_URI, {})
