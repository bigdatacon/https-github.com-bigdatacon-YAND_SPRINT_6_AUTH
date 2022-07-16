# http://localhost:5000/groups/test
# http://localhost:5000/groups/test_hello/
# http://localhost:5000/groups/
from flask import Blueprint, render_template, request
from flask.json import jsonify
from flask_jwt_extended import JWTManager
from db_models import User, Group
from auth_config import Config, db , jwt
from groups_bp import groups_bp
from users_bp import users_bp
from test_bp import test_bp
"""
Основной модуль
"""
import datetime
import logging
import os
import shutil
import sys
import time
import uuid
from flask import Flask


logger = logging.getLogger("auth_api")


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

    For both testing and working databases create admin group unless it already
    exists, then create admin user unless it already exists and add admin user
    to admin group if not already.

    In case ot the testing database create a testing group and a testing user.
    """
    if testing:
        # For testing database, delete all data first
        logger.info("Deleting all existing data before running tests")
        User.query.delete()
        Group.query.delete()
        db.session.commit()
    if Group.query.filter(Group.name=='admin').count() == 0:
        # For both testing and working database create admin group unless it already exists
        admin_group = Group(
            id = uuid.uuid4(),
            name='admin',
            description='admin'
        )
        db.session.add(admin_group)
        logger.info("Admin group created")
    else:
        admin_group = Group.query.filter(Group.name=='admin')[0]
        logger.info("Admin group already exists, unchanged")
    db.session.commit()
    if User.query.filter(User.login=='admin').count() == 0:
        # For both testing and working database create admin user unless it already exists
        admin_user = User(
            id = uuid.uuid4(),
            login="admin",
            email="admin@test.com",
            full_name="Admin",
            phone="8(123)4567890",
            address="MSK",
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        admin_user.password = 'admin'
        db.session.add(admin_user)
        logger.info("Admin user created")
    else:
        admin_user = User.query.filter(User.login=='admin')[0]
        logger.info("Admin user already exists, unchanged")
    db.session.commit()
    if admin_user in list(admin_group.users):
        logger.info("Admin user is already in admin group")
    else:
        admin_group.users.append(admin_user)
        logger.info("Admin user added to admin group")
    db.session.commit()
    if testing:
        first_group = Group(
            id = uuid.uuid4(),
            name='first',
            description='First testing group'
        )
        db.session.commit()


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        init_db()
        # При прогоне тестов удаляем прошлые данные из базы и создаем заново
        if len(sys.argv) == 2 and sys.argv[1] == "--testing":
            init_db(testing = True)
        elif len(sys.argv) == 2 and sys.argv[1] == "--working":
            init_db(testing = False)
        app.run(host="0.0.0.0")
