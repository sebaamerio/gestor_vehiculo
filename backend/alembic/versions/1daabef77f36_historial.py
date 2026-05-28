"""historial

Revision ID: 1daabef77f36
Revises: 3981e2ad2f56
Create Date: 2026-01-12 12:33:25.110022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1daabef77f36'
down_revision: Union[str, Sequence[str], None] = '3981e2ad2f56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

