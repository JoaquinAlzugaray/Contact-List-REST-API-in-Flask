"""empty message

Revision ID: 522ae7f563bc
Revises: b1630a717719
Create Date: 2022-03-08 20:43:13.530318

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '522ae7f563bc'
down_revision = 'b1630a717719'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('contact_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('group_id', 'contact_id')
    )
    op.drop_column('group', 'contacts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group', sa.Column('contacts', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_table('groups')
    # ### end Alembic commands ###
