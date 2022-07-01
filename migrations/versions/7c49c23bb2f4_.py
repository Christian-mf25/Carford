"""empty message

Revision ID: 7c49c23bb2f4
Revises: 
Create Date: 2022-07-01 11:18:16.458269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c49c23bb2f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_owners',
    sa.Column('cnh', sa.String(length=11), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('opportunity', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('cnh')
    )
    op.create_table('tb_cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=6), nullable=True),
    sa.Column('model', sa.String(length=11), nullable=True),
    sa.Column('owner_cnh', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['owner_cnh'], ['tb_owners.cnh'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_cars')
    op.drop_table('tb_owners')
    # ### end Alembic commands ###
