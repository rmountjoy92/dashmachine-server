from flask import Blueprint, jsonify, request
from app import dm

core = Blueprint("core", __name__)


@core.route("/register_client", methods=["GET"])
def register_client():
    return jsonify("success")


@core.route("/config", methods=["GET"])
def config():
    return jsonify(dm.config_json)


@core.route("/update_config", methods=["POST"])
def update_config():
    return jsonify(dm.modify_json(k=request.json.get("k"), v=request.json.get("v")))
