from pathlib import Path
from dotenv import load_dotenv
from .celery import app as celery_app

# Load environment variables
dotenv_path = Path(".").resolve() / ".env"
load_dotenv(dotenv_path)

# Make sure the app is always imported when Django starts so that shared_task will use this app.
__all__ = ("celery_app",)