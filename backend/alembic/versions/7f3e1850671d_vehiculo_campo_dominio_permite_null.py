"""vehiculo campo dominio permite null

Revision ID: 7f3e1850671d
Revises: 5206319c69f6
Create Date: 2025-11-29 08:15:22.654830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7f3e1850671d'
down_revision: Union[str, Sequence[str], None] = '5206319c69f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

