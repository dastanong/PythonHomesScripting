"""empty message

Revision ID: 76a343e44df7
Revises: 690282a2917a
Create Date: 2019-09-08 18:37:45.763472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76a343e44df7'
down_revision = '690282a2917a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sell_price', sa.Integer(), nullable=True),
    sa.Column('list_price', sa.Integer(), nullable=True),
    sa.Column('living', sa.Integer(), nullable=True),
    sa.Column('rooms', sa.Integer(), nullable=True),
    sa.Column('beds', sa.Integer(), nullable=True),
    sa.Column('bathrooms', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('arces', sa.Float(), nullable=True),
    sa.Column('taxes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('homes')
    # ### end Alembic commands ###