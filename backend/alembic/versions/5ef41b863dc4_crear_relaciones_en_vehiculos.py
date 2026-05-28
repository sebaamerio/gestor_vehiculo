"""crear relaciones en vehiculos

Revision ID: 5ef41b863dc4
Revises: 7f722de53aa9
Create Date: 2025-11-06 11:50:50.145615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '5ef41b863dc4'
down_revision: Union[str, Sequence[str], None] = '7f722de53aa9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

