"""Add industry column to users table

Revision ID: 6f612b779180
Revises: 1a8ea610fcbb
Create Date: 2025-03-05 20:41:28.093918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision: str = '6f612b779180'
down_revision: Union[str, None] = '1a8ea610fcbb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Apply the migration: Add industry column to users table"""
    op.add_column('users', sa.Column('industry', sa.String(), nullable=True))


def downgrade() -> None:
    """Rollback the migration: Remove industry column from users table"""
    op.drop_column('users', 'industry')
