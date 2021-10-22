import json
from app.paths import config_json


class DashMachine:
    def __init__(self):
        self.app = None

        # Set default configuration
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
        self.dashboards = [
            {
                "name": "DashMachine",
            }
        ]
        self.plugins = []

        # Overwrite default configuration with config.json
        self.config_json = {}
        self.apply_config()

        # write defaults to config json on first run
        if self.config_json == {}:
            self.modify_json("settings", self.settings)
            self.modify_json("users", self.users)
            self.modify_json("dashboards", self.dashboards)
            self.modify_json("plugins", self.plugins)

        print("DashMachine Initialized.")

    def apply_config(self):
        with open(config_json) as f:
            self.config_json = json.loads(f.read() or "{}")
        for k, v in self.config_json.items():
            setattr(self, k, v)

    def modify_json(self, k, v):
        with open(config_json) as f:
            data = json.loads(f.read() or "{}")

        data[k] = v

        with open(config_json, "w") as f:
            json.dump(data, f, indent=6)
        self.config_json = data
        for key, val in self.config_json.items():
            setattr(self, key, val)

        return getattr(self, k)

    def init_app(self, app):
        self.app = app
