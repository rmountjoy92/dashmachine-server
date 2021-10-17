from flask import Flask, jsonify, request
from .config import config
from .dashmachine import DashMachine

dm = DashMachine()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    dm.init_app(app)

    @app.errorhandler(500)
    def server_error(error):
        return (
            jsonify(
                {
                    "error": f"Error on {request.url}:\n {error.description}",
                    "code": error.code,
                    "name": error.name,
                    "orig_exception": error.original_exception,
                }
            ),
            500,
        )

    @app.errorhandler(404)
    def not_found_error(error):
        return (
            jsonify(
                {
                    "error": f"{request.url} Not found!",
                    "code": error.code,
                    "name": error.name,
                }
            ),
            404,
        )

    @app.errorhandler(401)
    def not_found_error(error):
        return (
            jsonify(
                {"error": f"Unauthorized!", "code": error.code, "name": error.name}
            ),
            401,
        )

    return app
