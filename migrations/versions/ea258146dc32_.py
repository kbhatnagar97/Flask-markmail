"""empty message

Revision ID: ea258146dc32
Revises: 5c5b95808bc7
Create Date: 2020-02-18 18:20:55.335062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea258146dc32'
down_revision = '5c5b95808bc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Customer_email'), 'Customer', ['email'], unique=True)
    op.create_index(op.f('ix_Customer_username'), 'Customer', ['username'], unique=True)
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=True)
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    op.drop_index(op.f('ix_Customer_username'), table_name='Customer')
    op.drop_index(op.f('ix_Customer_email'), table_name='Customer')
    op.drop_table('Customer')
    # ### end Alembic commands ###