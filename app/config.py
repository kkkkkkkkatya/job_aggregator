import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
POSTGRES_DB = os.getenv("POSTGRES_DB", "job_aggregator")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

POSTGRES_CONNECTION_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

TORTOISE_CONFIG = {
    "connections": {"default": POSTGRES_CONNECTION_URL},
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                "app.models",
            ],
            "default_connection": "default",
        }
    }
}

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

LOGGER_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console_generic': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'file_generic': {
            'format': '[%(asctime)s] [%(process)d] [%(levelname)s] [%(name)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'console_generic',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'file_generic',
            'filename': str(LOGS_DIR / 'app.log'),
            'maxBytes': 10485760,
            'backupCount': 5,
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        'app': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': False
        },
        'uvicorn.error': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': False
        },
        'uvicorn.access': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': False
        }
    }
}