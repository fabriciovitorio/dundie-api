"""ensure_admin_user

Revision ID: 162258584401
Revises: 005ee183d345
Create Date: 2024-04-07 15:44:03.794864

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel

from dundie.models.user import User
from sqlmodel import Session 


# revision identifiers, used by Alembic.
revision = '162258584401'
down_revision = '005ee183d345'
branch_labels = None
depends_on = None


def upgrade() -> None:  # NEW
    bind = op.get_bind()
    session = Session(bind=bind)

    admin = User(
        name="Admin",
        username="admin",
        email="admin@dm.com",
        dept="management",
        currency="USD",
        password="admin",  # pyright: ignore
    )
    # if admin user already exists it will raise IntegrityError
    try:
        session.add(admin)
        session.commit()
    except sa.exc.IntegrityError:
        session.rollback()


def downgrade() -> None:
    pass
