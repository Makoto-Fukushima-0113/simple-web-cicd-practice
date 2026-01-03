"""create demo items

Revision ID: 907f8d8cc7af
Revises:
Create Date: 2026-01-03

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "907f8d8cc7af"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "demo_items",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )

    # 動作確認用の1件
    op.execute("INSERT INTO demo_items (name) VALUES ('hello-from-alembic')")


def downgrade() -> None:
    op.drop_table("demo_items")
