"""novedad Infraccion

Revision ID: e8cd6c0dcf48
Revises: 08366f49716b
Create Date: 2026-04-03 09:30:41.997027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e8cd6c0dcf48'
down_revision: Union[str, Sequence[str], None] = '08366f49716b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

