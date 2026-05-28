"""Dependencias y Transferencias Historial

Revision ID: 5ca42292d131
Revises: b4bb015c01f8
Create Date: 2026-01-09 00:04:53.779998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ca42292d131'
down_revision: Union[str, Sequence[str], None] = 'b4bb015c01f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

