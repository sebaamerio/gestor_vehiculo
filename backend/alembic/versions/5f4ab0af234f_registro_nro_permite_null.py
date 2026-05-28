"""registro_nro permite null

Revision ID: 5f4ab0af234f
Revises: e074a717418f
Create Date: 2026-05-11

"""
from typing import Sequence, Union
from alembic import op

revision: str = '5f4ab0af234f'
down_revision: Union[str, Sequence[str], None] = 'e074a717418f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

