"""Fecha fin comodato_historial permita null

Revision ID: c92ff43c5551
Revises: b194f556ce14
Create Date: 2026-01-13 23:59:18.613424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c92ff43c5551'
down_revision: Union[str, Sequence[str], None] = 'b194f556ce14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

