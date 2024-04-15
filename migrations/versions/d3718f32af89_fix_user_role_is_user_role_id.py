"""fix: user.role_is = user.role_id

Revision ID: d3718f32af89
Revises: b4c65e196895
Create Date: 2024-04-15 15:20:20.195185

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3718f32af89'
down_revision: Union[str, None] = 'b4c65e196895'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=True))
    op.drop_constraint('user_role_is_fkey', 'user', type_='foreignkey')
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    op.drop_column('user', 'role_is')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role_is', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.create_foreign_key('user_role_is_fkey', 'user', 'role', ['role_is'], ['id'])
    op.drop_column('user', 'role_id')
    # ### end Alembic commands ###