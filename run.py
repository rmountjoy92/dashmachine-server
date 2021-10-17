import os
from app import create_app

if __name__ == "__main__":
    app = create_app(os.environ.get("CONFIG", None) or "development")
    app.run(host="0.0.0.0")
