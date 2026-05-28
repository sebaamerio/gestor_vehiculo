"""vehiculo se agrega campo guarda

Revision ID: 0c87394ec095
Revises: 67fbf58dbd93
Create Date: 2025-11-29 19:02:50.576913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c87394ec095'
down_revision: Union[str, Sequence[str], None] = '67fbf58dbd93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

