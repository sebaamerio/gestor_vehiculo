"""dependencia y vehiculo se cambio id y vehiculo_id a BigInteger

Revision ID: dadb84447777
Revises: 0da0d3842add
Create Date: 2025-11-09 01:02:43.937167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'dadb84447777'
down_revision: Union[str, Sequence[str], None] = '0da0d3842add'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

