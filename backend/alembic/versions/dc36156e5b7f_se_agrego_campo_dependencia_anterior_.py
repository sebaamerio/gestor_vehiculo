"""se agrego campo dependencia_anterior_descripcion a donaciones

Revision ID: dc36156e5b7f
Revises: 97ea1b9e5529
Create Date: 2026-03-24 23:06:26.148070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'dc36156e5b7f'
down_revision: Union[str, Sequence[str], None] = '97ea1b9e5529'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
