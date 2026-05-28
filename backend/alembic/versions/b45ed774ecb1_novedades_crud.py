"""Novedades CRUD

Revision ID: b45ed774ecb1
Revises: 8d22fb5f4cf6
Create Date: 2025-11-10 00:51:23.995725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b45ed774ecb1'
down_revision: Union[str, Sequence[str], None] = '8d22fb5f4cf6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

