from flask import Blueprint, render_template, request
from flask.json import jsonify
from db_models import  User, Group
# blueprint_auth = Blueprint(name="auth", url_prefix="/auth", import_name=__name__)


groups_bp = Blueprint("groups_bp", __name__)

@groups_bp.route("/test", methods=["GET"])
def list_groups_test():
    """
    тест
    """
    return jsonify("hello world")

@groups_bp.route("/test_hello/", methods=["GET"])
def hello_groups_test():
    """
    тест
    """
    return jsonify("hello")

@groups_bp.route("/", methods=["GET"])
def list_groups():
    """
    Список всех пользовательских групп
    """
    groups = []
    for group in Group.query.all():
        groups.append(group.to_json())
    return jsonify(groups)

print(list_groups)