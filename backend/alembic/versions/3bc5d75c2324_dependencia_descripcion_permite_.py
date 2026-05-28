"""dependencia descripcion permite duplicado

Revision ID: 3bc5d75c2324
Revises: ae5f0c8df72e
Create Date: 2025-11-09 00:20:37.039500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '3bc5d75c2324'
down_revision: Union[str, Sequence[str], None] = 'ae5f0c8df72e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

