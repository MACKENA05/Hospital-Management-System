"""instead of date changed to appointment_date

Revision ID: 61be0da51a92
Revises: e9eb27be589e
Create Date: 2025-03-09 21:32:46.867657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61be0da51a92'
down_revision: Union[str, None] = 'e9eb27be589e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('appointment_date', sa.DateTime(), nullable=False))
    op.drop_column('appointments', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('date', sa.DATETIME(), nullable=False))
    op.drop_column('appointments', 'appointment_date')
    # ### end Alembic commands ###
