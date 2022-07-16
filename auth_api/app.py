# http://localhost:5000/groups/test
# http://localhost:5000/groups/test_hello/
# http://localhost:5000/groups/
from flask import Blueprint, render_template, request
from flask.json import jsonify
from flask_jwt_extended import JWTManager
from auth_config import Config, db , jwt
from groups_bp import groups_bp
from users_bp import users_bp
from test_bp import test_bp
"""
Основной модуль
"""
import logging
import os
import shutil
import sys
import time
import uuid
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.register_blueprint(groups_bp, url_prefix=f"/groups")
    app.register_blueprint(users_bp, url_prefix=f"/users")
    app.register_blueprint(test_bp, url_prefix=f"/test")
    db.init_app(app)
    # app.register_blueprint(users_bp, url_prefix=f"{BASE_PATH}/users")
    # app.register_blueprint(test_bp, url_prefix="/test")


    # engine = db.create_engine(Config.SQLALCHEMY_DATABASE_URI, {})
    # engine.execute("CREATE SCHEMA IF NOT EXISTS auth;")
    # migrate_obj.init_app(app, db)
    jwt = JWTManager()
    jwt.init_app(app)

    return app


def init_db(testing: bool = False):
    """
    Initialize the database

    In case of the testing database, clear all existing data first.

    In case of working database, do nothing if database is currently not emply.
    Otherwise, create the admin group and the admin user.
    """
    if testing:
        # For testing database, delete all data first
        db.drop_all()
    if Group.query.filter(name='admin').count() == 0:
        # For both testing and working database create admin group unless it already exists
        admin_group = Group(
            id = uuid.uuid4(),
            name='admin',
            description='admin'
        )
        db.session.add(admin_group)
    else:
        admin_group = Group.query.filter(name='admin')[0]
    if User.query.filter(name='admin').count() == 0:
        # For both testing and working database create admin user unless it already exists
        admin_user = User(
            id = uuid.uuid4(),
            login="admin",
            email="admin@example.com",
            full_name="Admin",
            phone="8(123)4567890",
            address="MSK",
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        admin_user.password = 'admin'
        db.session.add(admin_user)
        admin_group.users.append(admin_user)
    db.session.commit()


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        init_db()
        # При прогоне тестов удаляем прошлые данные из базы и создаем заново
        if len(sys.argv) == 2 and sys.argv[1] == "--testing":
            init_db(testing = True)
        else:
            init_db(testing = False)
        app.run(host="0.0.0.0")
