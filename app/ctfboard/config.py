from datetime import datetime
from pytz import timezone
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "x^_2#w)m=0&+fzmw1oq-cd!75_g=z!1^*xd(@_zs=ync2(m-gl"

DEBUG = True
ALLOWED_HOSTS = ["platform.ugractf.ru", "127.0.0.1"]

COMPETITIONS = {
    "ctf": {
        "full_name": "Ugra CTF 2018",
        "start_time": datetime(2018, 6, 6, 4, 20, 0, 0, timezone("UTC")),
        "finish_time": datetime(2018, 6, 6, 7, 0, 0, 0, timezone("UTC")),
        "tasks_folder": os.path.join(BASE_DIR, "repo")
    },
    "spectators": {
        "full_name": "Ugra CTF 2018: Spectators",
        "start_time": datetime(2018, 6, 5, 11, 25, 50, 0, timezone("UTC")),
        "finish_time": datetime(2018, 6, 6, 14, 30, 0, 0, timezone("UTC")),
        "tasks_folder": os.path.join(BASE_DIR, "repo")
    }
}

BOARDS_URL = "/boards/"
BOARDS_ROOT = os.path.join(BASE_DIR, "boards")

DATABASE = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
