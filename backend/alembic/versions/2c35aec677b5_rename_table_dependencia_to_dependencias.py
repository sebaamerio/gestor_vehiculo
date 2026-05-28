"""rename table dependencia to dependencias

Revision ID: 2c35aec677b5
Revises: 5ca42292d131
Create Date: 2026-01-09 10:05:03.706690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2c35aec677b5'
down_revision: Union[str, Sequence[str], None] = '5ca42292d131'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

