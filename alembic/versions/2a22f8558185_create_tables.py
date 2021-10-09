"""create tables

Revision ID: 2a22f8558185
Revises: de29361780fb
Create Date: 2021-10-09 17:18:45.716102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a22f8558185'
down_revision = 'de29361780fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('receipt', sa.VARCHAR(length=255), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bill')
    # ### end Alembic commands ###
