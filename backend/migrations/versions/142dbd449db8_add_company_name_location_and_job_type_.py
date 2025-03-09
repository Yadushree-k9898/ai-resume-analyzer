"""Add company_name, location, and job_type columns to jobs table

Revision ID: 142dbd449db8
Revises: 07f5fc1a1b6c
Create Date: 2025-03-09 15:03:02.486074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '142dbd449db8'
down_revision: Union[str, None] = '07f5fc1a1b6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('jobs', sa.Column('company_name', sa.String(), nullable=False, server_default='Unknown Company'))
    op.add_column('jobs', sa.Column('location', sa.String(), nullable=False, server_default='Not specified'))
    op.add_column('jobs', sa.Column('job_type', sa.String(), nullable=False, server_default='Unknown'))



def downgrade() -> None:
    op.drop_column('jobs', 'job_type')
    op.drop_column('jobs', 'location')
    op.drop_column('jobs', 'company_name')
