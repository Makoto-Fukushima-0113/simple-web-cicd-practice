import os
from sqlalchemy import create_engine, text

def build_db_url() -> str:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db = os.getenv("DB_NAME")
    if not all([user, password, db]):
        raise RuntimeError(
            f"Missing env vars. user={bool(user)} pass={bool(password)} db={bool(db)}"
        )

    # Cloud Run（Cloud SQL 連携）: /cloudsql/<INSTANCE> の Unix socket を使う
    instance = os.getenv("INSTANCE_CONNECTION_NAME")
    if instance:
        return f"mysql+pymysql://{user}:{password}@localhost/{db}?unix_socket=/cloudsql/{instance}"

    # Cloud Build（Proxy）やローカル: TCP でつなぐ（デフォルトは Proxy の想定）
    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "3306")
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"

def fetch_latest_demo_item() -> str:
    engine = create_engine(build_db_url(), pool_pre_ping=True)
    with engine.connect() as conn:
        row = conn.execute(text("SELECT name FROM demo_items ORDER BY id DESC LIMIT 1")).fetchone()
        return row[0] if row else "(no rows)"
