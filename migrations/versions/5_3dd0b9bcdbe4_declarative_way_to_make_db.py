"""Declarative way to  make db

Revision ID: 3dd0b9bcdbe4
Revises: 3cd22bb9357a
Create Date: 2024-04-28 17:36:48.470886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dd0b9bcdbe4'
down_revision: Union[str, None] = '3cd22bb9357a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
