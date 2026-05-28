"""dependencia y vehiculo se cambio id y vehiculo_id a BigInteger

Revision ID: 0da0d3842add
Revises: 011d0693be17
Create Date: 2025-11-09 01:00:33.426197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0da0d3842add'
down_revision: Union[str, Sequence[str], None] = '011d0693be17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# p.drop_constraint("vehiculos_ibfk_8", "vehiculos", type_="foreignkey")

def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

