"""se agrego campo icon a la tabla tipo_condicion

Revision ID: ae5f0c8df72e
Revises: cc5c8205339b
Create Date: 2025-11-06 14:11:11.958372

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae5f0c8df72e'
down_revision: Union[str, Sequence[str], None] = 'cc5c8205339b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

