"""Create users and families tables

Revision ID: your_revision_id
Revises: None
Create Date: 2023-09-01 00:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = 'your_revision_id'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('users', sa.Column('profile_img', sa.String(length=50), nullable=True))

def downgrade():
    op.drop_column('users', 'profile_img')

