from flask import Blueprint, jsonify

core = Blueprint("core", __name__)


@core.route("/register_client", methods=["GET"])
def register_client():
    return jsonify("success")
