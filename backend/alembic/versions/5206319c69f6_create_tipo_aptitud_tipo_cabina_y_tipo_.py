"""create tipo_aptitud, tipo_cabina y tipo_traccion

Revision ID: 5206319c69f6
Revises: 114712de610c
Create Date: 2025-11-29 00:58:31.707337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '5206319c69f6'
down_revision: Union[str, Sequence[str], None] = '114712de610c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

