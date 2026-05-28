"""crear tabla tipo_situacion_chofer

Revision ID: 6d4f7a9605b5
Revises: c177d5a1b615
Create Date: 2026-02-27 10:06:35.926492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d4f7a9605b5'
down_revision: Union[str, Sequence[str], None] = 'c177d5a1b615'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

