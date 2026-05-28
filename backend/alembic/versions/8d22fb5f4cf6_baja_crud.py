"""Baja CRUD

Revision ID: 8d22fb5f4cf6
Revises: 3930bf00489a
Create Date: 2025-11-10 00:47:11.287039

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d22fb5f4cf6'
down_revision: Union[str, Sequence[str], None] = '3930bf00489a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

