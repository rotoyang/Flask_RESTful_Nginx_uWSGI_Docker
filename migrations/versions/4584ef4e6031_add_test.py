"""add test

Revision ID: 4584ef4e6031
Revises: 2821722f89f1
Create Date: 2021-08-30 23:56:10.196838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4584ef4e6031'
down_revision = '2821722f89f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    # ### end Alembic commands ###
