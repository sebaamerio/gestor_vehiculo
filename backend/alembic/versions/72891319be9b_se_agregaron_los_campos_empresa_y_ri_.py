"""Se agregaron los campos empresa y ri_anterior a vehiculo

Revision ID: 72891319be9b
Revises: 845919c3af1b
Create Date: 2026-04-26 01:24:02.606476

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '72891319be9b'
down_revision: Union[str, Sequence[str], None] = '845919c3af1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

