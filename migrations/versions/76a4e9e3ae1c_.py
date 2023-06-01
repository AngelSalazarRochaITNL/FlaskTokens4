"""empty message

Revision ID: 76a4e9e3ae1c
Revises: ca6820b726d9
Create Date: 2023-05-30 20:57:33.693364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76a4e9e3ae1c'
down_revision = 'ca6820b726d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donante', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tarjeta', sa.String(length=16), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donante', schema=None) as batch_op:
        batch_op.drop_column('tarjeta')

    # ### end Alembic commands ###