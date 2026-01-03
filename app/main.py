import os
from datetime import datetime, timezone
from flask import Flask
from app.db import fetch_latest_demo_item

app = Flask(__name__)

@app.get("/")
def index():
    env_name = os.getenv("ENV_NAME", "unknown")
    app_rev = os.getenv("APP_REV", "local")
    ts = datetime.now(timezone.utc).isoformat()

    sample_value = os.getenv("SAMPLE_VALUE", "no-db-yet")
    db_error = None
    try:
        sample_value = fetch_latest_demo_item()
    except Exception as e:
        db_error = repr(e)

    body = f"""
    <html>
      <body>
        <h2>simple-web</h2>
        <ul>
          <li>ENV_NAME: {env_name}</li>
          <li>APP_REV: {app_rev}</li>
          <li>SAMPLE_VALUE: {sample_value}</li>
          <li>timestamp(UTC): {ts}</li>
        </ul>
        {"<pre>DB_ERROR: "+db_error+"</pre>" if db_error else ""}
      </body>
    </html>
    """
    return body
