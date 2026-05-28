"""dependencia y vehiculo se cambio id y vehiculo_id a BigInteger

Revision ID: 011d0693be17
Revises: 273584da32ce
Create Date: 2025-11-09 00:55:30.639184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '011d0693be17'
down_revision: Union[str, Sequence[str], None] = '273584da32ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

