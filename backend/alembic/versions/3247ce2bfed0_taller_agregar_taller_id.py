"""Taller agregar taller_id

Revision ID: 3247ce2bfed0
Revises: 23f69df43aec
Create Date: 2025-11-10 23:52:53.407810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3247ce2bfed0'
down_revision: Union[str, Sequence[str], None] = '23f69df43aec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

