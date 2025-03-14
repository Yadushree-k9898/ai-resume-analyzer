"""Fix JobMatch import issue

Revision ID: f9a5ec1cc7c9
Revises: c128f1fee7cb
Create Date: 2025-03-14 11:11:26.053704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f9a5ec1cc7c9'
down_revision: Union[str, None] = 'c128f1fee7cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dashboard')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dashboard',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('total_resumes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('latest_resume_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('best_resume_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('resume_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('average_resume_score', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('total_jobs_applied', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('job_application_status', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('job_matches', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('total_job_matches', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('missing_skills', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('skills_analysis', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('last_updated', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['best_resume_id'], ['resumes.id'], name='dashboard_best_resume_id_fkey'),
    sa.ForeignKeyConstraint(['latest_resume_id'], ['resumes.id'], name='dashboard_latest_resume_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='dashboard_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='dashboard_pkey')
    )
    # ### end Alembic commands ###
