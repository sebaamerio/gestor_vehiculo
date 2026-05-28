"""unique dominio

Revision ID: 114712de610c
Revises: fb5e1ccfe0df
Create Date: 2025-11-27 10:12:54.818587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '114712de610c'
down_revision: Union[str, Sequence[str], None] = 'fb5e1ccfe0df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

