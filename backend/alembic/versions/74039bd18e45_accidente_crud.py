"""Accidente Crud

Revision ID: 74039bd18e45
Revises: f355bb400a59
Create Date: 2025-11-10 11:41:44.414030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74039bd18e45'
down_revision: Union[str, Sequence[str], None] = 'f355bb400a59'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

