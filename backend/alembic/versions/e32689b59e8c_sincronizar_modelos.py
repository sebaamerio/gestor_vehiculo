"""sincronizar modelos

Revision ID: e32689b59e8c
Revises: d46cf05ca264
Create Date: 2025-11-04 23:48:48.490014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e32689b59e8c'
down_revision: Union[str, Sequence[str], None] = 'd46cf05ca264'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

