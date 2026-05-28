"""Relaciones Vehiculo-Dependencias

Revision ID: a5a6be4224f3
Revises: b1ba1fabe46b
Create Date: 2026-01-08 00:27:24.086041

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5a6be4224f3'
down_revision: Union[str, Sequence[str], None] = 'b1ba1fabe46b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

