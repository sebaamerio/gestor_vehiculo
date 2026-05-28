"""historial

Revision ID: fcad1c091607
Revises: 1daabef77f36
Create Date: 2026-01-12 12:41:44.151262

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcad1c091607'
down_revision: Union[str, Sequence[str], None] = '1daabef77f36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

