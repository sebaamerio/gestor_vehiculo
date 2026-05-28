"""Tabla Tipo de Pago

Revision ID: b40df7cb35a6
Revises: fb3e69e71935
Create Date: 2026-03-28 17:30:16.370741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b40df7cb35a6'
down_revision: Union[str, Sequence[str], None] = 'fb3e69e71935'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

