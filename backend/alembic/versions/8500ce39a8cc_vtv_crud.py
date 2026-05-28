"""vtv CRUD

Revision ID: 8500ce39a8cc
Revises: dadb84447777
Create Date: 2025-11-09 19:38:16.945517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8500ce39a8cc'
down_revision: Union[str, Sequence[str], None] = 'dadb84447777'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

