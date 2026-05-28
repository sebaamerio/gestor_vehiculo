"""dependencia y vehiculo se cambio id y vehiculo_id a BigInteger

Revision ID: 273584da32ce
Revises: d8a3e87d2bbe
Create Date: 2025-11-09 00:52:49.661185

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '273584da32ce'
down_revision: Union[str, Sequence[str], None] = 'd8a3e87d2bbe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

