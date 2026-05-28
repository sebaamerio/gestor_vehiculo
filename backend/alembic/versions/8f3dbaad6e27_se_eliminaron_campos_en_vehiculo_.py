"""Se eliminaron campos en vehiculo_dependencia

Revision ID: 8f3dbaad6e27
Revises: 2569f2092545
Create Date: 2026-03-29 10:59:38.063744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '8f3dbaad6e27'
down_revision: Union[str, Sequence[str], None] = '2569f2092545'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

