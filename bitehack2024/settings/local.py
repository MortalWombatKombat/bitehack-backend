from .base import *

SECRET_KEY = "secret_key"

# ------------- DATABASES -------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "bitehack2024"),
        "USER": env("POSTGRES_USER", "bitehack2024"),
        "PASSWORD": env("POSTGRES_PASSWORD", "bitehack2024"),
        "HOST": env("POSTGRES_HOST", "localhost"),
    }
}
