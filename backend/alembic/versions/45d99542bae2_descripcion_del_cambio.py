"""descripcion del cambio

Revision ID: 45d99542bae2
Revises: 320cdd63ea65
Create Date: 2025-11-04 23:57:42.561955

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45d99542bae2'
down_revision: Union[str, Sequence[str], None] = '320cdd63ea65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

