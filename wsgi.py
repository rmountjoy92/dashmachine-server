import os
from app import create_app

app = create_app(os.environ.get("CONFIG", None) or "default")
