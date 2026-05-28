"""add_roles_and_users_tables

Revision ID: e074a717418f
Revises: 72891319be9b
Create Date: 2026-05-08 18:38:10.449237

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e074a717418f'
down_revision: Union[str, Sequence[str], None] = '72891319be9b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

