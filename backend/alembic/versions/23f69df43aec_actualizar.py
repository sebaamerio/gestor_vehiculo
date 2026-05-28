"""Actualizar

Revision ID: 23f69df43aec
Revises: bd7011f0d4ac
Create Date: 2025-11-10 23:02:09.751390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23f69df43aec'
down_revision: Union[str, Sequence[str], None] = 'bd7011f0d4ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

