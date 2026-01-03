import os
from sqlalchemy import create_engine, text

def build_db_url() -> str:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db = os.getenv("DB_NAME")
    # Cloud Run + Cloud SQL Proxy(Unix socket) 前提
    instance = os.getenv("INSTANCE_CONNECTION_NAME")
    if not all([user, password, db, instance]):
        raise RuntimeError(f"Missing env vars. user={bool(user)} pass={bool(password)} db={bool(db)} instance={bool(instance)}")

    return f"mysql+pymysql://{user}:{password}@localhost/{db}?unix_socket=/cloudsql/{instance}"

def fetch_latest_demo_item() -> str:
    engine = create_engine(build_db_url(), pool_pre_ping=True)
    with engine.connect() as conn:
        row = conn.execute(text("SELECT name FROM demo_items ORDER BY id DESC LIMIT 1")).fetchone()
        return row[0] if row else "(no rows)"
