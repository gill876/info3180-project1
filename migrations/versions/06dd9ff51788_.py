"""empty message

Revision ID: 06dd9ff51788
Revises: 
Create Date: 2020-03-30 02:25:19.019400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06dd9ff51788'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=80), nullable=True),
    sa.Column('lname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=150), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('biography', sa.String(length=500), nullable=True),
    sa.Column('filename', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###
