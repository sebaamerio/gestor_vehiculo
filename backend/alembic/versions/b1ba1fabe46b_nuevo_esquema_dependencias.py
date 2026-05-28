"""Nuevo esquema Dependencias

Revision ID: b1ba1fabe46b
Revises: 900f4c34b6d1
Create Date: 2026-01-07 23:56:21.934263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1ba1fabe46b'
down_revision: Union[str, Sequence[str], None] = '900f4c34b6d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

