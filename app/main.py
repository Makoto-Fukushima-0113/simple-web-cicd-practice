import os
from datetime import datetime, timezone
from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    env_name = os.getenv("ENV_NAME", "unknown")
    now = datetime.now(timezone.utc).isoformat()

    # いまはDB未接続（後続でCloud SQL + Alembicを入れる）
    sample_value = os.getenv("SAMPLE_VALUE", "no-db-yet")

    return f"""
    <html>
      <body>
        <h2>simple-web</h2>
        <ul>
          <li>ENV_NAME: {env_name}</li>
          <li>SAMPLE_VALUE: {sample_value}</li>
          <li>timestamp(UTC): {now}</li>
        </ul>
      </body>
    </html>
    """

@app.get("/healthz")
def healthz():
    return "ok", 200
