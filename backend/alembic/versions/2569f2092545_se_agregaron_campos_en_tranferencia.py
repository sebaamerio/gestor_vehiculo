"""Se agregaron campos en Tranferencia

Revision ID: 2569f2092545
Revises: b40df7cb35a6
Create Date: 2026-03-29 10:05:16.003072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2569f2092545'
down_revision: Union[str, Sequence[str], None] = 'b40df7cb35a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

