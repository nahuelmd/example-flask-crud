"""Initial migration.

Revision ID: cd0bc48737c4
Revises: 
Create Date: 2024-01-16 00:32:41.543316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd0bc48737c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('entry', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_entry_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_title'), ['title'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entry', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_entry_title'))
        batch_op.drop_index(batch_op.f('ix_entry_description'))

    op.drop_table('entry')
    # ### end Alembic commands ###
