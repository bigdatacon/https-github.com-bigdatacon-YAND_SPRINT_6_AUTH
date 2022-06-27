from flask import Blueprint, render_template, request
from flask.json import jsonify
from db_models import  User, Group
users_bp = Blueprint("users_bp", __name__)

@users_bp.route("/", methods=["GET"])
def list_groups():
    """
    Список всех пользователей
    """
    users = []
    for user in User.query.all():
        users.append(user.to_json())
    return jsonify(users)
