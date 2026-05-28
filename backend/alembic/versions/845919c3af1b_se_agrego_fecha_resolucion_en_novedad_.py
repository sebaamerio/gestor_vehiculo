"""Se agrego fecha_resolucion en novedad donacion

Revision ID: 845919c3af1b
Revises: 8849b09acedd
Create Date: 2026-04-24 00:15:17.685228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '845919c3af1b'
down_revision: Union[str, Sequence[str], None] = '8849b09acedd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

