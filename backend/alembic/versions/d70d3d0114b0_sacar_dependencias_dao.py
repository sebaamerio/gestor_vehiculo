"""Sacar Dependencias Dao

Revision ID: d70d3d0114b0
Revises: 6a7b2ee0fcfb
Create Date: 2026-01-07 19:04:49.061738

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd70d3d0114b0'
down_revision: Union[str, Sequence[str], None] = '6a7b2ee0fcfb'
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
