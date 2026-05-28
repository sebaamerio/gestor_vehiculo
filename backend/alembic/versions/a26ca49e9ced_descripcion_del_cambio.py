"""descripcion del cambio

Revision ID: a26ca49e9ced
Revises: 45d99542bae2
Create Date: 2025-11-05 00:24:03.483906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a26ca49e9ced'
down_revision: Union[str, Sequence[str], None] = '45d99542bae2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

