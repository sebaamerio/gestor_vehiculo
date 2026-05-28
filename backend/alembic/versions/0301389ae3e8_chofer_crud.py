"""Chofer Crud

Revision ID: 0301389ae3e8
Revises: b45ed774ecb1
Create Date: 2025-11-10 10:44:55.819022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0301389ae3e8'
down_revision: Union[str, Sequence[str], None] = 'b45ed774ecb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

