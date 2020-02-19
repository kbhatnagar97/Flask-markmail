"""empty message

Revision ID: 1ff1677213f9
Revises: 489d0c086127
Create Date: 2020-02-19 01:19:46.810956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ff1677213f9'
down_revision = '489d0c086127'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Customer', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.add_column('Customer', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_Customer_username'), 'Customer', ['username'], unique=True)
    op.drop_index('ix_Customer_address', table_name='Customer')
    op.drop_index('ix_Customer_age', table_name='Customer')
    op.drop_index('ix_Customer_first_name', table_name='Customer')
    op.drop_index('ix_Customer_gender', table_name='Customer')
    op.drop_index('ix_Customer_last_name', table_name='Customer')
    op.drop_index('ix_Customer_phoneNumber', table_name='Customer')
    op.drop_index('ix_Customer_registrationDate', table_name='Customer')
    op.drop_index('ix_Customer_state', table_name='Customer')
    op.drop_index('ix_Customer_zipcode', table_name='Customer')
    op.drop_column('Customer', 'last_name')
    op.drop_column('Customer', 'phoneNumber')
    op.drop_column('Customer', 'zipcode')
    op.drop_column('Customer', 'registrationDate')
    op.drop_column('Customer', 'first_name')
    op.drop_column('Customer', 'age')
    op.drop_column('Customer', 'gender')
    op.drop_column('Customer', 'address')
    op.drop_column('Customer', 'state')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Customer', sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Customer', sa.Column('address', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Customer', sa.Column('gender', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Customer', sa.Column('age', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Customer', sa.Column('first_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Customer', sa.Column('registrationDate', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Customer', sa.Column('zipcode', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Customer', sa.Column('phoneNumber', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Customer', sa.Column('last_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.create_index('ix_Customer_zipcode', 'Customer', ['zipcode'], unique=True)
    op.create_index('ix_Customer_state', 'Customer', ['state'], unique=True)
    op.create_index('ix_Customer_registrationDate', 'Customer', ['registrationDate'], unique=True)
    op.create_index('ix_Customer_phoneNumber', 'Customer', ['phoneNumber'], unique=True)
    op.create_index('ix_Customer_last_name', 'Customer', ['last_name'], unique=True)
    op.create_index('ix_Customer_gender', 'Customer', ['gender'], unique=True)
    op.create_index('ix_Customer_first_name', 'Customer', ['first_name'], unique=True)
    op.create_index('ix_Customer_age', 'Customer', ['age'], unique=True)
    op.create_index('ix_Customer_address', 'Customer', ['address'], unique=True)
    op.drop_index(op.f('ix_Customer_username'), table_name='Customer')
    op.drop_column('Customer', 'username')
    op.drop_column('Customer', 'password_hash')
    # ### end Alembic commands ###
