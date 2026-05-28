"""tablas

Revision ID: 8ac99d1a2ad4
Revises: fcad1c091607
Create Date: 2026-01-12 12:42:31.887620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ac99d1a2ad4'
down_revision: Union[str, Sequence[str], None] = 'fcad1c091607'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

