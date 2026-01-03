import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

def build_db_url() -> str | None:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    dbname = os.getenv("DB_NAME")
    if not (user and password and dbname):
        return None

    instance = os.getenv("INSTANCE_CONNECTION_NAME")
    if instance:
        socket_path = f"/cloudsql/{instance}"
        return f"mysql+pymysql://{user}:{password}@/{dbname}?unix_socket={socket_path}"

    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "3306")
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"

def get_engine() -> Engine | None:
    url = build_db_url()
    if not url:
        return None
    return create_engine(url, pool_pre_ping=True)
