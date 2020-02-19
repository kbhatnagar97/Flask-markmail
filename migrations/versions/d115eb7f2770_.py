"""empty message

Revision ID: d115eb7f2770
Revises: 8b8915c82721
Create Date: 2020-02-19 16:15:07.495531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd115eb7f2770'
down_revision = '8b8915c82721'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Customer', sa.Column('registerationDate', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_Customer_registerationDate'), 'Customer', ['registerationDate'], unique=True)
    op.drop_index('ix_Customer_registrationDate', table_name='Customer')
    op.drop_column('Customer', 'registrationDate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Customer', sa.Column('registrationDate', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.create_index('ix_Customer_registrationDate', 'Customer', ['registrationDate'], unique=True)
    op.drop_index(op.f('ix_Customer_registerationDate'), table_name='Customer')
    op.drop_column('Customer', 'registerationDate')
    # ### end Alembic commands ###