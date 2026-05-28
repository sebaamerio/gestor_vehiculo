"""Robo Crud

Revision ID: 56956a9841f5
Revises: 938c9caba3d2
Create Date: 2025-11-10 13:56:19.256433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56956a9841f5'
down_revision: Union[str, Sequence[str], None] = '938c9caba3d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

