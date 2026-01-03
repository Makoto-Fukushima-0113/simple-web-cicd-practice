from alembic import op
import sqlalchemy as sa

def upgrade() -> None:
    op.create_table(
        "demo_items",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("message", sa.String(length=200), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    )
    op.execute("INSERT INTO demo_items (message) VALUES ('hello from alembic')")

def downgrade() -> None:
    op.drop_table("demo_items")
