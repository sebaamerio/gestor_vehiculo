"""crear tabla tipo_situacion_chofer

Revision ID: 0ab56ed33972
Revises: c0664b0156a3
Create Date: 2026-02-27 09:48:30.617958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ab56ed33972'
down_revision: Union[str, Sequence[str], None] = 'c0664b0156a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

