"""init schema

Revision ID: 784ebb370323
Revises: 172a565bc28d
Create Date: 2025-11-04 10:06:45.697544

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '784ebb370323'
down_revision: Union[str, Sequence[str], None] = '172a565bc28d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

