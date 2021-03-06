"""empty message

Revision ID: 1e6e58e9af1d
Revises: 8bf791900f53
Create Date: 2017-01-13 19:58:32.869461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e6e58e9af1d'
down_revision = '8bf791900f53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('law_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('law',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('content', sa.String(length=1000), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proposal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('poster_id', sa.Integer(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['poster_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('law_law_status',
    sa.Column('law_id', sa.Integer(), nullable=True),
    sa.Column('law_status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['law_id'], ['law.id'], ),
    sa.ForeignKeyConstraint(['law_status_id'], ['law_status.id'], )
    )
    op.create_table('law_proposal',
    sa.Column('law_id', sa.Integer(), nullable=True),
    sa.Column('proposal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['law_id'], ['law.id'], ),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], )
    )
    op.create_table('proposal_downvote',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('proposal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('proposal_upvote',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('proposal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('proposal_upvote')
    op.drop_table('proposal_downvote')
    op.drop_table('law_proposal')
    op.drop_table('law_law_status')
    op.drop_table('proposal')
    op.drop_table('law')
    op.drop_table('law_status')
    # ### end Alembic commands ###
