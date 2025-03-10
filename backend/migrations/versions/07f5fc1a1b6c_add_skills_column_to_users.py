"""Add skills column to users

Revision ID: 07f5fc1a1b6c
Revises: 6f612b779180
Create Date: 2025-03-05 20:50:06.931603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '07f5fc1a1b6c'
down_revision: Union[str, None] = '6f612b779180'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_resumes_id', table_name='resumes')
    op.drop_table('resumes')
    op.drop_index('ix_job_applications_id', table_name='job_applications')
    op.drop_table('job_applications')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_jobs_id', table_name='jobs')
    op.drop_table('jobs')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jobs',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('jobs_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('skills_required', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='jobs_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_jobs_id', 'jobs', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('role', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('reset_token', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('reset_token_expires', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('two_factor_enabled', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('two_factor_secret', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('job_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('industry', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=True)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.create_table('job_applications',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('job_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('applied_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], name='job_applications_job_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='job_applications_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='job_applications_pkey')
    )
    op.create_index('ix_job_applications_id', 'job_applications', ['id'], unique=False)
    op.create_table('resumes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('file_path', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('extracted_text', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('resume_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('parsed_skills', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('job_matches', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('improvement_suggestions', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='resumes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='resumes_pkey')
    )
    op.create_index('ix_resumes_id', 'resumes', ['id'], unique=False)
    # ### end Alembic commands ###
