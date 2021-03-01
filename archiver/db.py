import logging
import os
from os import environ

import sqlalchemy
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)
logger.debug("Loading SQLAlchemy {}".format(sqlalchemy.__version__))

DB_HOST = environ.get("DB_HOST")
DB_PORT = environ.get("DB_PORT")
DB_NAME = environ.get("DB_NAME")
DB_USER = environ.get("DB_USER")
DB_PASS = environ.get("DB_PASS")

engine = create_engine(
    "postgresql://{}:{}@{}:{}/{}".format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
)

# Load all models
path = os.path.join(".", "models")
for py in [
    f[:-3] for f in os.listdir(path) if f.endswith(".py") and f != "__init__.py"
]:
    model_path = ".".join(["models", py])
    mod = __import__(model_path, fromlist=[py])

    classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
    for cls in classes:
        logger.debug("Loading model {} from {}".format(cls, model_path))
