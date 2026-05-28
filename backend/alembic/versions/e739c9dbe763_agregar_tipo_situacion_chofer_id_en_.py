"""agregar tipo_situacion_chofer_id en choferes

Revision ID: e739c9dbe763
Revises: be68c4f46877
Create Date: 2026-02-27 11:29:22.113795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e739c9dbe763'
down_revision: Union[str, Sequence[str], None] = 'be68c4f46877'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass


def downgrade():
    pass

