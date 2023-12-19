"""empty message

Revision ID: 5327b0ee4137
Revises: 4e043ab38b0a
Create Date: 2023-12-08 20:14:07.627052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5327b0ee4137'
down_revision: Union[str, None] = '4e043ab38b0a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_cat', sa.String(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.Column('photo_link', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cat')
    # ### end Alembic commands ###
