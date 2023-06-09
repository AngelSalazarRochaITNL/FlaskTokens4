"""empty message

Revision ID: ca6820b726d9
Revises: 97d734c9b2be
Create Date: 2023-05-30 20:48:41.121463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca6820b726d9'
down_revision = '97d734c9b2be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donante', schema=None) as batch_op:
        batch_op.drop_column('cardno')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donante', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cardno', sa.INTEGER(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
