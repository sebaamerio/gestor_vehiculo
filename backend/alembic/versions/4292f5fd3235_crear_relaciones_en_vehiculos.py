"""crear relaciones en vehiculos

Revision ID: 4292f5fd3235
Revises: 7be0041ddacb
Create Date: 2025-11-06 12:02:51.454012

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '4292f5fd3235'
down_revision: Union[str, Sequence[str], None] = '7be0041ddacb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

