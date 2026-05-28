"""crear tabla tipo_situacion_chofer

Revision ID: be68c4f46877
Revises: 6d4f7a9605b5
Create Date: 2026-02-27 11:00:01.673875

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be68c4f46877'
down_revision: Union[str, Sequence[str], None] = '6d4f7a9605b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass


def downgrade():
    pass
