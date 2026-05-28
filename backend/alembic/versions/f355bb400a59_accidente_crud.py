"""Accidente Crud

Revision ID: f355bb400a59
Revises: 3dc6539bbb55
Create Date: 2025-11-10 11:39:05.287382

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'f355bb400a59'
down_revision: Union[str, Sequence[str], None] = '3dc6539bbb55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

