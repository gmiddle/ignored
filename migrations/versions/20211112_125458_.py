"""empty message

Revision ID: 3fa5ceaaaa59
Revises: afa4f9a76e7c
Create Date: 2021-11-12 12:54:58.629003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fa5ceaaaa59'
down_revision = 'afa4f9a76e7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('private_servers', sa.Column('ownerId', sa.Integer()))
    op.create_foreign_key(None, 'private_servers', 'users', ['ownerId'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'private_servers', type_='foreignkey')
    op.drop_column('private_servers', 'ownerId')
    # ### end Alembic commands ###