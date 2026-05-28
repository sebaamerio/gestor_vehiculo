"""crear tipos

Revision ID: d46cf05ca264
Revises: 19b988c13a72
Create Date: 2025-11-04 23:47:15.668642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd46cf05ca264'
down_revision: Union[str, Sequence[str], None] = '19b988c13a72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

