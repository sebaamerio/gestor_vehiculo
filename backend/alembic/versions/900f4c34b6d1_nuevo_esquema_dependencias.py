"""Nuevo esquema Dependencias

Revision ID: 900f4c34b6d1
Revises: d70d3d0114b0
Create Date: 2026-01-07 22:36:45.206559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '900f4c34b6d1'
down_revision: Union[str, Sequence[str], None] = 'd70d3d0114b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

