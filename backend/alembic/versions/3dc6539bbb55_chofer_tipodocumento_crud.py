"""Chofer tipoDocumento Crud

Revision ID: 3dc6539bbb55
Revises: 0301389ae3e8
Create Date: 2025-11-10 10:50:49.667830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dc6539bbb55'
down_revision: Union[str, Sequence[str], None] = '0301389ae3e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

