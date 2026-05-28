"""Vehiculo permitir null en campos

Revision ID: fb5e1ccfe0df
Revises: 3247ce2bfed0
Create Date: 2025-11-11 17:12:47.030289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'fb5e1ccfe0df'
down_revision: Union[str, Sequence[str], None] = '3247ce2bfed0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

