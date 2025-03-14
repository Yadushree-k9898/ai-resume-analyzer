"""Add resume_id to job_matches

Revision ID: a87385ec9fb1
Revises: 323a779102a1
Create Date: 2025-03-13 17:27:13.886806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision: str = 'a87385ec9fb1'
down_revision: Union[str, None] = '323a779102a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Populate resume_id with default values
    op.execute("UPDATE job_matches SET resume_id = (SELECT id FROM resumes LIMIT 1) WHERE resume_id IS NULL")
    
    # Make resume_id non-nullable
    op.alter_column('job_matches', 'resume_id', nullable=False)
    
    # Alter missing_skills column type
    op.alter_column('job_matches', 'missing_skills',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               type_=sa.String(),
               existing_nullable=True,
               existing_server_default=sa.text("'[]'::jsonb"))

    # Check if the foreign key constraint already exists before creating it
    conn = op.get_bind()
    result = conn.execute(
        text("SELECT conname FROM pg_constraint WHERE conname = 'fk_job_matches_resume'")
    ).fetchone()

    if not result:
        op.create_foreign_key('fk_job_matches_resume', 'job_matches', 'resumes', ['resume_id'], ['id'])

def downgrade():
    op.alter_column('job_matches', 'missing_skills',
        type_=sa.Text(),
        existing_type=sa.dialects.postgresql.JSONB,
        postgresql_using="missing_skills::text"  # Explicit cast to TEXT
    )
