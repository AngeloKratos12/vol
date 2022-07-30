"""create tables

Revision ID: 474f5767b64b
Revises: 
Create Date: 2022-07-30 15:17:37.670747

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '474f5767b64b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=True),
    sa.Column('prenom', sa.String(length=50), nullable=True),
    sa.Column('mail', sa.String(length=50), nullable=True),
    sa.Column('telephone', sa.String(length=15), nullable=True),
    sa.Column('cin', sa.String(length=15), nullable=True),
    sa.Column('nbr_passage', sa.Integer(), nullable=True),
    sa.Column('categorie', mysql.ENUM('vol', 'reservation'), nullable=True),
    sa.Column('voyage', mysql.ENUM('national', 'International'), nullable=True),
    sa.Column('date_voyage', sa.Date(), nullable=True),
    sa.Column('heurre_voyage', sa.Time(), nullable=True),
    sa.Column('payement', mysql.ENUM('mvola', 'carte_bank'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_id'), 'client', ['id'], unique=False)
    op.create_table('reservation_international',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=True),
    sa.Column('prenom', sa.String(length=50), nullable=True),
    sa.Column('mail', sa.String(length=50), nullable=True),
    sa.Column('telephone', sa.String(length=15), nullable=True),
    sa.Column('cin', sa.String(length=15), nullable=True),
    sa.Column('nbr_passage', sa.Integer(), nullable=True),
    sa.Column('destination', mysql.ENUM('paris', 'bordeau'), nullable=True),
    sa.Column('date_voyage', sa.Date(), nullable=True),
    sa.Column('heurre_voyage', sa.Time(), nullable=True),
    sa.Column('payement', mysql.ENUM('mvola', 'carte_bank'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reservation_international_id'), 'reservation_international', ['id'], unique=False)
    op.create_table('reservation_national',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=True),
    sa.Column('prenom', sa.String(length=50), nullable=True),
    sa.Column('mail', sa.String(length=50), nullable=True),
    sa.Column('telephone', sa.String(length=15), nullable=True),
    sa.Column('cin', sa.String(length=15), nullable=True),
    sa.Column('nbr_passage', sa.Integer(), nullable=True),
    sa.Column('destination', mysql.ENUM('mahajanga', 'tamatave', 'diego'), nullable=True),
    sa.Column('date_voyage', sa.Date(), nullable=True),
    sa.Column('heurre_voyage', sa.Time(), nullable=True),
    sa.Column('payement', mysql.ENUM('mvola', 'carte_bank'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reservation_national_id'), 'reservation_national', ['id'], unique=False)
    op.create_table('vol_international',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=True),
    sa.Column('prenom', sa.String(length=50), nullable=True),
    sa.Column('mail', sa.String(length=50), nullable=True),
    sa.Column('telephone', sa.String(length=15), nullable=True),
    sa.Column('cin', sa.String(length=15), nullable=True),
    sa.Column('nbr_passage', sa.Integer(), nullable=True),
    sa.Column('destination', mysql.ENUM('paris', 'bordeau'), nullable=True),
    sa.Column('date_voyage', sa.Date(), nullable=True),
    sa.Column('heurre_voyage', sa.Time(), nullable=True),
    sa.Column('payement', mysql.ENUM('mvola', 'carte_bank'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vol_international_id'), 'vol_international', ['id'], unique=False)
    op.create_table('vol_national',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=True),
    sa.Column('prenom', sa.String(length=50), nullable=True),
    sa.Column('mail', sa.String(length=50), nullable=True),
    sa.Column('telephone', sa.String(length=15), nullable=True),
    sa.Column('cin', sa.String(length=15), nullable=True),
    sa.Column('nbr_passage', sa.Integer(), nullable=True),
    sa.Column('destination', mysql.ENUM('mahajanga', 'tamatave', 'diego'), nullable=True),
    sa.Column('date_voyage', sa.Date(), nullable=True),
    sa.Column('heurre_voyage', sa.Time(), nullable=True),
    sa.Column('payement', mysql.ENUM('mvola', 'carte_bank'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vol_national_id'), 'vol_national', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vol_national_id'), table_name='vol_national')
    op.drop_table('vol_national')
    op.drop_index(op.f('ix_vol_international_id'), table_name='vol_international')
    op.drop_table('vol_international')
    op.drop_index(op.f('ix_reservation_national_id'), table_name='reservation_national')
    op.drop_table('reservation_national')
    op.drop_index(op.f('ix_reservation_international_id'), table_name='reservation_international')
    op.drop_table('reservation_international')
    op.drop_index(op.f('ix_client_id'), table_name='client')
    op.drop_table('client')
    # ### end Alembic commands ###
