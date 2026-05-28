"""la localidad_id en comodato_historial permita null

Revision ID: 8dceed3e3e2b
Revises: c92ff43c5551
Create Date: 2026-01-14 00:04:00.817055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '8dceed3e3e2b'
down_revision: Union[str, Sequence[str], None] = 'c92ff43c5551'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

