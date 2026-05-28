"""eliminar tipo_situacion de choferes

Revision ID: 84b88d67b5d4
Revises: e739c9dbe763
Create Date: 2026-02-27 18:26:41.742258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84b88d67b5d4'
down_revision: Union[str, Sequence[str], None] = 'e739c9dbe763'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass


def downgrade() -> None:
    pass

