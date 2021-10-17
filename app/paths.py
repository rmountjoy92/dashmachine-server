import os
from pathlib import Path


# root path of the application
def get_root_folder():
    curr_folder = os.path.dirname(__file__)
    rfolder = Path(curr_folder).parent
    return rfolder


def make_file(path):
    if not os.path.isfile(path):
        with open(path, "w") as new_file:
            new_file.write("")


def make_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


root_folder = get_root_folder()

app_folder = os.path.join(root_folder, "app")

config_folder = os.path.join(root_folder, "config")
make_dir(config_folder)

config_json = os.path.join(config_folder, "config.json")
make_file(config_json)
