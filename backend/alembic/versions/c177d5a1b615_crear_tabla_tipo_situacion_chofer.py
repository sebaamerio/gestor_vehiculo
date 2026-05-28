"""crear tabla tipo_situacion_chofer

Revision ID: c177d5a1b615
Revises: 0ab56ed33972
Create Date: 2026-02-27 09:58:37.511345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c177d5a1b615'
down_revision: Union[str, Sequence[str], None] = '0ab56ed33972'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

