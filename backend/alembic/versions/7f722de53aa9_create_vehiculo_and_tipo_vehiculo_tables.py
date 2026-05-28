"""create vehiculo and tipo_vehiculo tables

Revision ID: 7f722de53aa9
Revises: a26ca49e9ced
Create Date: 2025-11-05 13:44:12.137386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7f722de53aa9'
down_revision: Union[str, Sequence[str], None] = 'a26ca49e9ced'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

