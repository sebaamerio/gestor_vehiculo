"""cambio en tipos de datos

Revision ID: 6a7b2ee0fcfb
Revises: 0c87394ec095
Create Date: 2025-12-02 01:03:28.691780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '6a7b2ee0fcfb'
down_revision: Union[str, Sequence[str], None] = '0c87394ec095'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

