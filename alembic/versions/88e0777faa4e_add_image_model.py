"""Add image model

Revision ID: 88e0777faa4e
Revises: 
Create Date: 2021-11-04 13:53:06.328124

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '88e0777faa4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'image',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('data', mysql.MEDIUMBLOB(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('image')
