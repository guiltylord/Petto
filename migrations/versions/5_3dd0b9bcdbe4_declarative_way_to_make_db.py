"""Declarative way to  make db

Revision ID: 3dd0b9bcdbe4
Revises: b555e19e282f
Create Date: 2024-04-28 17:36:48.470886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3dd0b9bcdbe4"
down_revision: Union[str, None] = "b555e19e282f"
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