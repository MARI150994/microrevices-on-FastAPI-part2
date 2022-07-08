"""change type of fields in provider table and type of article field in product table

Revision ID: 8b9b7719e7bf
Revises: 8536d41ecd97
Create Date: 2022-07-06 13:27:48.684614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b9b7719e7bf'
down_revision = '8536d41ecd97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'article',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('provider', 'email',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('provider', 'phone',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('provider', 'phone',
               existing_type=sa.String(),
               type_=sa.BOOLEAN(),
               existing_nullable=False)
    op.alter_column('provider', 'email',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('product', 'article',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
