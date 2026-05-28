"""crear tabla tipo_situacion_chofer

Revision ID: c0664b0156a3
Revises: 8dceed3e3e2b
Create Date: 2026-02-27 09:41:41.015351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0664b0156a3'
down_revision: Union[str, Sequence[str], None] = '8dceed3e3e2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

