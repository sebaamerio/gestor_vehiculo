"""descripcion del cambio

Revision ID: 320cdd63ea65
Revises: e32689b59e8c
Create Date: 2025-11-04 23:50:23.317196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '320cdd63ea65'
down_revision: Union[str, Sequence[str], None] = 'e32689b59e8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

