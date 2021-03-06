# http://localhost:5000/groups/test
# http://localhost:5000/groups/test_hello/
# http://localhost:5000/auth/groups/
from flask import Blueprint, render_template, request
from flask.json import jsonify
from auth_config import Config, db
from groups_bp import groups_bp
"""
Основной модуль
"""
import logging
import os
import shutil
import sys
import time
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.register_blueprint(groups_bp, url_prefix=f"/groups")
    db.init_app(app)
    # app.register_blueprint(users_bp, url_prefix=f"{BASE_PATH}/users")
    # app.register_blueprint(test_bp, url_prefix="/test")


    # engine = db.create_engine(Config.SQLALCHEMY_DATABASE_URI, {})
    # engine.execute("CREATE SCHEMA IF NOT EXISTS auth;")
    # jwt.init_app(app)
    # migrate_obj.init_app(app, db)

    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        # # При прогоне тестов удаляем прошлые данные из базы и создаем заново
        # if len(sys.argv) == 2 and sys.argv[1] == "--reinitialize":
        #     db.drop_all()
        # # Инициалиазции базы. Проверяем наличие таблицы пользователей
        # if not insp.has_table("user", schema="auth"):
        #     logging.info(f"initializing...")
        #     db_initialize(app)
        app.run(host="0.0.0.0")