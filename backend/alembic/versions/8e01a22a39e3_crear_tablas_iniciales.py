"""crear tablas iniciales

Revision ID: 8e01a22a39e3
Revises: 784ebb370323
Create Date: 2025-11-04 10:12:48.996946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e01a22a39e3'
down_revision: Union[str, Sequence[str], None] = '784ebb370323'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

