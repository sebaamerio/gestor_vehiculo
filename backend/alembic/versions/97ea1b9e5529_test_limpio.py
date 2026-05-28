"""test limpio

Revision ID: 97ea1b9e5529
Revises: c00412deb59c
Create Date: 2026-03-17 21:49:41.239904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '97ea1b9e5529'
down_revision: Union[str, Sequence[str], None] = 'c00412deb59c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
