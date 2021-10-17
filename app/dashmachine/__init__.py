import json
from app.paths import config_json


class DashMachine:
    def __init__(self):
        self.app = None
        self.users = [{"username": "admin", "password": "admin", "role": "admin"}]
        self.settings = {
            "theme": {
                "primary": "orange",
                "accent": "light-blue",
                "on-primary": "white",
                "secondary": "grey",
                "dark": "auto",
            },
            "roles": ["admin"],
        }
        self.dashboards = []
        self.plugins = []

        with open(config_json) as f:
            self.config_json = json.loads(f.read() or "{}")

        for k, v in self.config_json.items():
            setattr(self, k, v)
        print("DashMachine Initialized.")

    def init_app(self, app):
        self.app = app
