"""dependencia-vehiculo

Revision ID: d909550ade73
Revises: 2c35aec677b5
Create Date: 2026-01-09 10:35:35.076743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd909550ade73'
down_revision: Union[str, Sequence[str], None] = '2c35aec677b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

