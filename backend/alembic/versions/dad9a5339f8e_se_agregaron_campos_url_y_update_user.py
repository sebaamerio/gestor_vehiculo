"""Se agregaron campos url y update_user

Revision ID: dad9a5339f8e
Revises: e8cd6c0dcf48
Create Date: 2026-04-04 18:55:40.193695

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'dad9a5339f8e'
down_revision: Union[str, Sequence[str], None] = 'e8cd6c0dcf48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

