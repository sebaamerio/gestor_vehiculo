"""drop dependencia_dao table

Revision ID: a1b2c3d4e5f6
Revises: 5f4ab0af234f
Create Date: 2026-05-15 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = '5f4ab0af234f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_index('ix_dependencia_dao_id', table_name='dependencia_dao', if_exists=True)
    op.drop_table('dependencia_dao', if_exists=True)


def downgrade() -> None:
    op.create_table(
        'dependencia_dao',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )   
