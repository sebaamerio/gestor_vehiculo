"""Eliminar campo de Vehiculo_Dependencia

Revision ID: 08366f49716b
Revises: 8f3dbaad6e27
Create Date: 2026-03-29 18:46:28.385724

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '08366f49716b'
down_revision: Union[str, Sequence[str], None] = '8f3dbaad6e27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

