"""localidad descripcion permite duplicado

Revision ID: b8e01f2f94bb
Revises: 3bc5d75c2324
Create Date: 2025-11-09 00:29:43.627812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8e01f2f94bb'
down_revision: Union[str, Sequence[str], None] = '3bc5d75c2324'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

