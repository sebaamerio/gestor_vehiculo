"""vehiculo longitud de campos

Revision ID: 67fbf58dbd93
Revises: 7f3e1850671d
Create Date: 2025-11-29 18:56:00.185674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '67fbf58dbd93'
down_revision: Union[str, Sequence[str], None] = '7f3e1850671d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

