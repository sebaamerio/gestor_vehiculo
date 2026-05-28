"""Dependencias y Transferencias Historial

Revision ID: b4bb015c01f8
Revises: f6a412196daa
Create Date: 2026-01-08 23:58:55.110113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4bb015c01f8'
down_revision: Union[str, Sequence[str], None] = 'f6a412196daa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

