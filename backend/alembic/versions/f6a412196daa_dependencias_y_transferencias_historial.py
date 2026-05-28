"""Dependencias y Transferencias Historial

Revision ID: f6a412196daa
Revises: a5a6be4224f3
Create Date: 2026-01-08 23:56:54.075461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6a412196daa'
down_revision: Union[str, Sequence[str], None] = 'a5a6be4224f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

