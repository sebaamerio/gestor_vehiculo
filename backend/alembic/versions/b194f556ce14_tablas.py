"""tablas

Revision ID: b194f556ce14
Revises: 8ac99d1a2ad4
Create Date: 2026-01-12 12:53:34.253254

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b194f556ce14'
down_revision: Union[str, Sequence[str], None] = '8ac99d1a2ad4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

