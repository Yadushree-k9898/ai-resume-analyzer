"""Add job_title column

Revision ID: 1a8ea610fcbb
Revises: 50d386caf8f0
Create Date: 2025-03-05 20:30:38.336314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a8ea610fcbb'
down_revision = '50d386caf8f0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('job_title', sa.String(), nullable=True))  # ✅ Add the missing column


def downgrade() -> None:
    op.drop_column('users', 'job_title')  # ✅ Remove the column if rolling back
