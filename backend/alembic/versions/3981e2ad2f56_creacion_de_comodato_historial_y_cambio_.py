"""creacion de comodato_historial y cambio de nombre tabla tipo_transferencia

Revision ID: 3981e2ad2f56
Revises: d909550ade73
Create Date: 2026-01-12 11:36:18.101082

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '3981e2ad2f56'
down_revision: Union[str, Sequence[str], None] = 'd909550ade73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

