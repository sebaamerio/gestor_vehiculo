"""Novedad Comodato

Revision ID: fb3e69e71935
Revises: dc36156e5b7f
Create Date: 2026-03-28 16:27:43.597854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'fb3e69e71935'
down_revision: Union[str, Sequence[str], None] = 'dc36156e5b7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

