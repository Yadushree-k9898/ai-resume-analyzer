"""Added phone_number field to User

Revision ID: 50d386caf8f0
Revises: 43f26b6ce880
Create Date: 2025-03-05 15:16:04.541314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '50d386caf8f0'
down_revision: Union[str, None] = '43f26b6ce880'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add the phone_number column to the users table.
    op.add_column('public.users', sa.Column('phone_number', sa.String(), nullable=True))

    # No indexes or tables are dropped in this migration.


def downgrade() -> None:
    # Remove the phone_number column from the users table.
    op.drop_column('users', 'phone_number')
    # No indexes or tables are recreated.
