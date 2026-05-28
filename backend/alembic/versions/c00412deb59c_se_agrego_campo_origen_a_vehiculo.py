"""Se agrego campo origen a vehiculo

Revision ID: c00412deb59c
Revises: 84b88d67b5d4
Create Date: 2026-03-02 13:31:46.691426

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c00412deb59c'
down_revision: Union[str, Sequence[str], None] = '84b88d67b5d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

