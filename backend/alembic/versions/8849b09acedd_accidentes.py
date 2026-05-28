"""accidentes

Revision ID: 8849b09acedd
Revises: dad9a5339f8e
Create Date: 2026-04-20 22:58:10.424917

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '8849b09acedd'
down_revision: Union[str, Sequence[str], None] = 'dad9a5339f8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

