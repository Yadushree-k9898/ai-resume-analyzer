from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'bd3e34c55a5d'
down_revision = 'ce8c1af9c80c'
branch_labels = None
depends_on = None

def upgrade():
    # Step 1: Add column with nullable=True
    op.add_column('jobs', sa.Column('apply_link', sa.String(), nullable=True))
    
    # Step 2: Set a default value for existing rows
    op.execute("UPDATE jobs SET apply_link = 'https://example.com' WHERE apply_link IS NULL")
    
    # Step 3: Alter column to be NOT NULL
    op.alter_column('jobs', 'apply_link', nullable=False)

def downgrade():
    op.drop_column('jobs', 'apply_link')
