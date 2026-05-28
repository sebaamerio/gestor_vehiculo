"""relaciones null en vehiculos

Revision ID: cc5c8205339b
Revises: 4292f5fd3235
Create Date: 2025-11-06 12:09:34.271847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'cc5c8205339b'
down_revision: Union[str, Sequence[str], None] = '4292f5fd3235'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

