"""modelo descripcion permite duplicado

Revision ID: d8a3e87d2bbe
Revises: b8e01f2f94bb
Create Date: 2025-11-09 00:39:45.906540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8a3e87d2bbe'
down_revision: Union[str, Sequence[str], None] = 'b8e01f2f94bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

