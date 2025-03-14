# from alembic import op
# import sqlalchemy as sa

# # Revision identifiers
# revision = '559a56dd134e'
# down_revision = 'a238f69a28d4'

# def upgrade():
#     # Step 1: Add column as nullable
#     op.add_column('jobs', sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=True))

#     # Step 2: Assign a valid default value
#     op.execute("""
#         UPDATE jobs 
#         SET user_id = (SELECT id FROM users LIMIT 1) 
#         WHERE user_id IS NULL
#     """)

#     # Step 3: Ensure column is NOT NULL
#     op.alter_column('jobs', 'user_id', nullable=False)

# def downgrade():
#     op.drop_column('jobs', 'user_id')



from alembic import op
import sqlalchemy as sa

# Revision identifiers
revision = '559a56dd134e'
down_revision = 'a238f69a28d4'

def upgrade():
    # Step 1: Add column as nullable
    op.add_column('jobs', sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=True))

    # Step 2: Assign a default user_id (existing user ID)
    op.execute("UPDATE jobs SET user_id = 1 WHERE user_id IS NULL")

    # Step 3: Ensure column is NOT NULL
    op.alter_column('jobs', 'user_id', nullable=False)

def downgrade():
    op.drop_column('jobs', 'user_id')
