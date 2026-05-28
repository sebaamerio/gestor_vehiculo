"""test migracion

Revision ID: 19b988c13a72
Revises: 8e01a22a39e3
Create Date: 2025-11-04 10:28:36.160149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19b988c13a72'
down_revision: Union[str, Sequence[str], None] = '8e01a22a39e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

