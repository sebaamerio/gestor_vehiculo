"""crear relaciones en vehiculos

Revision ID: 7be0041ddacb
Revises: 5ef41b863dc4
Create Date: 2025-11-06 11:54:12.944368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7be0041ddacb'
down_revision: Union[str, Sequence[str], None] = '5ef41b863dc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

