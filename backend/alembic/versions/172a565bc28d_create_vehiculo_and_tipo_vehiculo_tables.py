"""initial schema

Revision ID: 172a565bc28d
Revises:
Create Date: 2025-11-04 09:59:14.097701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '172a565bc28d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing = set(inspector.get_table_names())
    schema_tables = {
        'roles', 'provincias', 'vehiculos', 'novedades', 'vtv',
        'reparaciones', 'vehiculo_dependencia', 'bajas', 'cambio_motor',
        'cambio_chasis', 'accidentes', 'donaciones', 'robos',
        'transferencias', 'comodato', 'infracciones',
    }
    if existing & schema_tables:
        return  # alguna tabla del esquema ya existe, no recrear

    # ── Tablas de lookup independientes ───────────────────────────────────

    op.create_table('roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre', sa.String(length=50), nullable=False),
        sa.Column('descripcion', sa.String(length=200), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('nombre'),
    )
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)

    op.create_table('provincias',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_provincias_id'), 'provincias', ['id'], unique=False)

    op.create_table('tipo_acto',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_acto_id'), 'tipo_acto', ['id'], unique=False)

    op.create_table('tipo_aptitud',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_aptitud_id'), 'tipo_aptitud', ['id'], unique=False)

    op.create_table('tipo_cabina',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_cabina_id'), 'tipo_cabina', ['id'], unique=False)

    op.create_table('tipo_carroceria',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_carroceria_id'), 'tipo_carroceria', ['id'], unique=False)

    op.create_table('tipo_condicion',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.Column('icon', sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
        sa.UniqueConstraint('icon'),
    )
    op.create_index(op.f('ix_tipo_condicion_id'), 'tipo_condicion', ['id'], unique=False)

    op.create_table('tipo_documento',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_documento_id'), 'tipo_documento', ['id'], unique=False)

    op.create_table('tipo_marca',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_marca_id'), 'tipo_marca', ['id'], unique=False)

    op.create_table('tipo_motor',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_motor_id'), 'tipo_motor', ['id'], unique=False)

    op.create_table('tipo_novedad',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_novedad_id'), 'tipo_novedad', ['id'], unique=False)

    op.create_table('tipo_pago',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_pago_id'), 'tipo_pago', ['id'], unique=False)

    op.create_table('tipo_reparacion_estado',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_reparacion_estado_id'), 'tipo_reparacion_estado', ['id'], unique=False)

    op.create_table('tipo_situacion',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_situacion_id'), 'tipo_situacion', ['id'], unique=False)

    op.create_table('tipo_situacion_chofer',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_situacion_chofer_id'), 'tipo_situacion_chofer', ['id'], unique=False)

    op.create_table('tipo_traccion',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_traccion_id'), 'tipo_traccion', ['id'], unique=False)

    op.create_table('tipo_tramite_dependencia',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_tramite_dependencia_id'), 'tipo_tramite_dependencia', ['id'], unique=False)

    op.create_table('tipo_vehiculo',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_vehiculo_id'), 'tipo_vehiculo', ['id'], unique=False)

    op.create_table('tipo_vtv_resultado',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descripcion'),
    )
    op.create_index(op.f('ix_tipo_vtv_resultado_id'), 'tipo_vtv_resultado', ['id'], unique=False)

    op.create_table('talleres',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('taller_desc', sa.String(length=150), nullable=False),
        sa.Column('domicilio', sa.String(length=100), nullable=True),
        sa.Column('cuit', sa.String(length=20), nullable=True),
        sa.Column('ing_brutos', sa.String(length=20), nullable=True),
        sa.Column('observaciones', sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('taller_desc'),
    )
    op.create_index(op.f('ix_talleres_id'), 'talleres', ['id'], unique=False)

    op.create_table('dependencias',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_dependencias_id'), 'dependencias', ['id'], unique=False)

    op.create_table('dependencia_dao',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('descripcion', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    # ── Tablas con FK a lookup tables ──────────────────────────────────────

    op.create_table('localidades',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=150), nullable=False),
        sa.Column('partido_id', sa.String(length=5), nullable=False),
        sa.Column('cod_postal', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('provincia_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['provincia_id'], ['provincias.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_localidades_id'), 'localidades', ['id'], unique=False)

    op.create_table('tipo_modelo',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(length=150), nullable=False),
        sa.Column('marca_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['marca_id'], ['tipo_marca.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_tipo_modelo_id'), 'tipo_modelo', ['id'], unique=False)

    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre', sa.String(length=100), nullable=False),
        sa.Column('username', sa.String(length=80), nullable=False),
        sa.Column('email', sa.String(length=150), nullable=False),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('activo', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username'),
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)

    op.create_table('choferes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('tipo_documento_id', sa.Integer(), nullable=True),
        sa.Column('documento', sa.String(length=20), nullable=True),
        sa.Column('nombre', sa.String(length=150), nullable=False),
        sa.Column('cargo', sa.Integer(), nullable=True),
        sa.Column('licencia', sa.String(length=50), nullable=True),
        sa.Column('dependencia_id', sa.BigInteger(), nullable=True),
        sa.Column('domicilio', sa.String(length=255), nullable=True),
        sa.Column('localidad_id', sa.Integer(), nullable=True),
        sa.Column('telefono', sa.String(length=50), nullable=True),
        sa.Column('tipo_situacion_chofer_id', sa.Integer(), nullable=True),
        sa.Column('observacion', sa.String(length=255), nullable=True),
        sa.Column('clase', sa.Integer(), nullable=True),
        sa.Column('fecha_nacimiento', sa.Date(), nullable=True),
        sa.Column('licencia_vto', sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(['tipo_documento_id'], ['tipo_documento.id'], ),
        sa.ForeignKeyConstraint(['localidad_id'], ['localidades.id'], ),
        sa.ForeignKeyConstraint(['tipo_situacion_chofer_id'], ['tipo_situacion_chofer.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_choferes_id'), 'choferes', ['id'], unique=False)

    # ── vehiculos (depende de las 10 tablas tipo_*) ────────────────────────

    op.create_table('vehiculos',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('registro_nro', sa.Integer(), nullable=True),
        sa.Column('registro_marca', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('fecha_titulo', sa.Date(), nullable=True),
        sa.Column('anio', sa.Integer(), nullable=True),
        sa.Column('plazas', sa.Integer(), nullable=True),
        sa.Column('carga', sa.Integer(), nullable=True),
        sa.Column('ejes', sa.SmallInteger(), nullable=True),
        sa.Column('motor_marca', sa.String(length=80), nullable=True),
        sa.Column('motor_nro', sa.String(length=80), nullable=False),
        sa.Column('dominio', sa.String(length=8), nullable=True),
        sa.Column('dominio_anterior', sa.String(length=8), nullable=True),
        sa.Column('chasis_marca', sa.String(length=80), nullable=True),
        sa.Column('chasis_nro', sa.String(length=40), nullable=False),
        sa.Column('fechaVtv', sa.Date(), nullable=True),
        sa.Column('observaciones', sa.String(length=150), nullable=True),
        sa.Column('tipo_dominio', sa.String(length=1), nullable=True),
        sa.Column('guarda', sa.String(length=30), nullable=True),
        sa.Column('titulo_certificado_url', sa.String(length=255), nullable=True),
        sa.Column('cedula_certificado_url', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('update_user', sa.String(length=100), nullable=True),
        sa.Column('origen', sa.String(length=60), nullable=True),
        sa.Column('empresa', sa.String(length=60), nullable=True),
        sa.Column('ri_anterior', sa.Integer(), nullable=True),
        sa.Column('marca_id', sa.Integer(), nullable=True),
        sa.Column('modelo_id', sa.Integer(), nullable=True),
        sa.Column('tipo_vehiculo_id', sa.Integer(), nullable=True),
        sa.Column('carroceria_id', sa.Integer(), nullable=True),
        sa.Column('tipo_motor_id', sa.Integer(), nullable=True),
        sa.Column('condicion_id', sa.Integer(), nullable=True),
        sa.Column('situacion_id', sa.Integer(), nullable=True),
        sa.Column('tipo_aptitud_id', sa.Integer(), nullable=True),
        sa.Column('tipo_cabina_id', sa.Integer(), nullable=True),
        sa.Column('tipo_traccion_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['marca_id'], ['tipo_marca.id'], ),
        sa.ForeignKeyConstraint(['modelo_id'], ['tipo_modelo.id'], ),
        sa.ForeignKeyConstraint(['tipo_vehiculo_id'], ['tipo_vehiculo.id'], ),
        sa.ForeignKeyConstraint(['carroceria_id'], ['tipo_carroceria.id'], ),
        sa.ForeignKeyConstraint(['tipo_motor_id'], ['tipo_motor.id'], ),
        sa.ForeignKeyConstraint(['condicion_id'], ['tipo_condicion.id'], ),
        sa.ForeignKeyConstraint(['situacion_id'], ['tipo_situacion.id'], ),
        sa.ForeignKeyConstraint(['tipo_aptitud_id'], ['tipo_aptitud.id'], ),
        sa.ForeignKeyConstraint(['tipo_cabina_id'], ['tipo_cabina.id'], ),
        sa.ForeignKeyConstraint(['tipo_traccion_id'], ['tipo_traccion.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('dominio'),
        sa.UniqueConstraint('registro_nro'),
        sa.UniqueConstraint('ri_anterior'),
    )
    op.create_index(op.f('ix_vehiculos_id'), 'vehiculos', ['id'], unique=False)

    # ── Tablas dependientes de vehiculos ───────────────────────────────────

    op.create_table('novedades',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('vehiculo_id', sa.BigInteger(), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('tipo_novedad_id', sa.Integer(), nullable=False),
        sa.Column('observaciones', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('update_user', sa.String(length=100), nullable=True),
        sa.ForeignKeyConstraint(['vehiculo_id'], ['vehiculos.id'], ),
        sa.ForeignKeyConstraint(['tipo_novedad_id'], ['tipo_novedad.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_novedades_id'), 'novedades', ['id'], unique=False)

    op.create_table('vtv',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('fecha_solicitud', sa.Date(), nullable=True),
        sa.Column('fecha_realizada', sa.Date(), nullable=True),
        sa.Column('fecha_vto', sa.Date(), nullable=True),
        sa.Column('zona', sa.SmallInteger(), nullable=True),
        sa.Column('oblea', sa.String(length=50), nullable=True),
        sa.Column('observaciones', sa.String(length=100), nullable=True),
        sa.Column('vtv_certificado_url', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('update_user', sa.String(length=100), nullable=True),
        sa.Column('vehiculo_id', sa.BigInteger(), nullable=False),
        sa.Column('tipo_vtvResultado_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['vehiculo_id'], ['vehiculos.id'], ),
        sa.ForeignKeyConstraint(['tipo_vtvResultado_id'], ['tipo_vtv_resultado.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_vtv_id'), 'vtv', ['id'], unique=False)

    op.create_table('reparaciones',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=True),
        sa.Column('factura', sa.String(length=50), nullable=True),
        sa.Column('fecha_pres', sa.Date(), nullable=True),
        sa.Column('detalle', sa.String(length=255), nullable=True),
        sa.Column('importe', sa.Numeric(precision=12, scale=2), nullable=True),
        sa.Column('caract', sa.String(length=50), nullable=True),
        sa.Column('expediente', sa.String(length=50), nullable=True),
        sa.Column('anioexp', sa.Integer(), nullable=True),
        sa.Column('alcance', sa.String(length=50), nullable=True),
        sa.Column('nrocuerpo', sa.String(length=50), nullable=True),
        sa.Column('km', sa.Integer(), nullable=True),
        sa.Column('update_user', sa.String(length=100), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('vehiculo_id', sa.BigInteger(), nullable=False),
        sa.Column('tipo_reparacion_estado_id', sa.Integer(), nullable=True),
        sa.Column('taller_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['vehiculo_id'], ['vehiculos.id'], ),
        sa.ForeignKeyConstraint(['tipo_reparacion_estado_id'], ['tipo_reparacion_estado.id'], ),
        sa.ForeignKeyConstraint(['taller_id'], ['talleres.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_reparaciones_id'), 'reparaciones', ['id'], unique=False)

    op.create_table('vehiculo_dependencia',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('fecha_desde', sa.Date(), nullable=False),
        sa.Column('fecha_hasta', sa.Date(), nullable=True),
        sa.Column('dependencia_descripcion', sa.String(length=100), nullable=True),
        sa.Column('activo', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('update_user', sa.String(length=60), nullable=True),
        sa.Column('vehiculo_id', sa.BigInteger(), nullable=False),
        sa.Column('dependencia_id', sa.BigInteger(), nullable=True),
        sa.Column('tipo_tramite_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['vehiculo_id'], ['vehiculos.id'], ),
        sa.ForeignKeyConstraint(['dependencia_id'], ['dependencias.id'], ),
        sa.ForeignKeyConstraint(['tipo_tramite_id'], ['tipo_tramite_dependencia.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_vehiculo_dependencia_id'), 'vehiculo_dependencia', ['id'], unique=False)

    # ── Tablas de novedades (dependientes de novedades) ────────────────────

    op.create_table('bajas',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('novedad_id', sa.Integer(), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('expediente', sa.String(length=50), nullable=True),
        sa.Column('informe', sa.String(length=50), nullable=True),
        sa.Column('acto_id', sa.Integer(), nullable=True),
        sa.Column('norma', sa.String(length=50), nullable=True),
        sa.ForeignKeyConstraint(['novedad_id'], ['novedades.id'], ),
        sa.ForeignKeyConstraint(['acto_id'], ['tipo_acto.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('novedad_id'),
    )
    op.create_index(op.f('ix_bajas_id'), 'bajas', ['id'], unique=False)

    op.create_table('cambio_motor',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('novedad_id', sa.Integer(), nullable=False),
        sa.Column('motor_nro_anterior', sa.String(length=50), nullable=False),
        sa.Column('motor_nro_nuevo', sa.String(length=50), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('expediente', sa.String(length=50), nullable=True),
        sa.Column('informe', sa.String(length=50), nullable=True),
        sa.Column('acto_id', sa.Integer(), nullable=True),
        sa.Column('norma', sa.String(length=50), nullable=True),
        sa.ForeignKeyConstraint(['novedad_id'], ['novedades.id'], ),
        sa.ForeignKeyConstraint(['acto_id'], ['tipo_acto.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('novedad_id'),
    )
    op.create_index(op.f('ix_cambio_motor_id'), 'cambio_motor', ['id'], unique=False)

    op.create_table('cambio_chasis',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('novedad_id', sa.Integer(), nullable=False),
        sa.Column('chasis_anterior', sa.String(length=50), nullable=False),
        sa.Column('chasis_nuevo', sa.String(length=50), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('expediente', sa.String(length=50), nullable=True),
        sa.Column('informe', sa.String(length=50), nullable=True),
        sa.Column('acto_id', sa.Integer(), nullable=True),
        sa.Column('norma', sa.String(length=50), nullable=True),
        sa.ForeignKeyConstraint(['novedad_id'], ['novedades.id'], ),
        sa.ForeignKeyConstraint(['acto_id'], ['tipo_acto.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('novedad_id'),
    )
    op.create_index(op.f('ix_cambio_chasis_id'), 'cambio_chasis', ['id'], unique=False)

    op.create_table('accidentes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('novedad_id', sa.Integer(), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('expediente', sa.String(length=50), nullable=True),
        sa.Column('informe', sa.String(length=50), nullable=True),
        sa.Column('acto_id', sa.Integer(), nullable=True),
        sa.Column('norma', sa.String(length=50), nullable=True),
        sa.Column('chofer_id', sa.Integer(), nullable=True),
        sa.Column('localidad_id', sa.Integer(), nullable=True),
        sa.Column('fecha_inicio_sumario', sa.Date(), nullable=True),
        sa.Column('fecha_fin_sumario', sa.Date(), nullable=True),
        sa.Column('lugar', sa.String(length=100), nullable=True),
        sa.ForeignKeyConstraint(['novedad_id'], ['novedades.id'], ),
        sa.ForeignKeyConstraint(['acto_id'], ['tipo_acto.id'], ),
        sa.ForeignKeyConstraint(['chofer_id'], ['choferes.id'], ),
        sa.ForeignKeyConstraint(['localidad_id'], ['localidades.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('novedad_id'),
    )
    op.create_index(op.f('ix_accidentes_id'), 'accidentes', ['id'], unique=False)

    op.create_table('donaciones',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('novedad_id', sa.Integer(), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('expediente', sa.String(length=50), nullable=True),
        sa.Column('informe', sa.String(length=50), nullable=True),
        sa.Column('acto_id', sa.Integer(), nullable=True),
        sa.Column('norma', sa.String(length=50), nullable=True),
        sa.Column('destino', sa.String(length=150), nullable=True),
        sa.Column('localidad_id', sa.Integer(), nullable=True),
        sa.Column('fecha_resolucion', sa.Date(), nullable=True),
        sa.Column('fecha_entrega', sa.Date(), nullable=True),
        sa.Column('fecha_formulario', sa.Date(), nullable=True),
        sa.Column('fecha_finalizado', sa.Date(), nullable=True),
        sa.Column('dependencia_anterior_id', sa.Integer(), nullable=True),
        sa.Column('dependencia_anterior_descripcion', sa.String(length=100), nullable=True),
        sa.ForeignKeyConstraint(['novedad_id'], ['novedades.id'], ),
        sa.ForeignKeyConstraint(['acto_id'], ['tipo_acto.id'], ),
        sa.ForeignKeyConstraint(['localidad_id'], ['localidades.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('novedad_id'),
    )
    op.create_index(op.f('ix_donaciones_id'), 'donaciones', ['id'], unique=False)

    op.create_table('robos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('novedad_id', sa.Integer(), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('expediente', sa.String(length=50), nullable=True),
        sa.Column('informe', sa.String(length=50), nullable=True),
        sa.Column('acto_id', sa.Integer(), nullable=True),
        sa.Column('norma', sa.String(length=50), nullable=True),
        sa.Column('chofer_id', sa.Integer(), nullable=True),
        sa.Column('localidad_id', sa.Integer(), nullable=True),
        sa.Column('fecha_recupero', sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(['novedad_id'], ['novedades.id'], ),
        sa.ForeignKeyConstraint(['acto_id'], ['tipo_acto.id'], ),
        sa.ForeignKeyConstraint(['chofer_id'], ['choferes.id'], ),
        sa.ForeignKeyConstraint(['localidad_id'], ['localidades.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('novedad_id'),
    )
    op.create_index(op.f('ix_robos_id'), 'robos', ['id'], unique=False)

    op.create_table('transferencias',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('novedad_id', sa.Integer(), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('expediente', sa.String(length=50), nullable=True),
        sa.Column('informe', sa.String(length=50), nullable=True),
        sa.Column('acto_id', sa.Integer(), nullable=True),
        sa.Column('norma', sa.String(length=50), nullable=True),
        sa.Column('dependencia_anterior_id', sa.BigInteger(), nullable=True),
        sa.Column('dependencia_anterior_descripcion', sa.String(length=100), nullable=True),
        sa.Column('dependencia_id', sa.BigInteger(), nullable=True),
        sa.Column('dependencia_descripcion', sa.String(length=100), nullable=True),
        sa.ForeignKeyConstraint(['novedad_id'], ['novedades.id'], ),
        sa.ForeignKeyConstraint(['acto_id'], ['tipo_acto.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('novedad_id'),
    )
    op.create_index(op.f('ix_transferencias_id'), 'transferencias', ['id'], unique=False)

    op.create_table('comodato',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('novedad_id', sa.Integer(), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('dependencia_id', sa.Integer(), nullable=True),
        sa.Column('dependencia_descripcion', sa.String(length=100), nullable=True),
        sa.Column('fecha_fin', sa.Date(), nullable=True),
        sa.Column('destino', sa.String(length=150), nullable=True),
        sa.Column('expediente', sa.String(length=50), nullable=True),
        sa.Column('informe', sa.String(length=50), nullable=True),
        sa.Column('localidad_id', sa.Integer(), nullable=True),
        sa.Column('acto_id', sa.Integer(), nullable=True),
        sa.Column('norma', sa.String(length=50), nullable=True),
        sa.ForeignKeyConstraint(['novedad_id'], ['novedades.id'], ),
        sa.ForeignKeyConstraint(['acto_id'], ['tipo_acto.id'], ),
        sa.ForeignKeyConstraint(['localidad_id'], ['localidades.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('novedad_id'),
    )
    op.create_index(op.f('ix_comodato_id'), 'comodato', ['id'], unique=False)

    op.create_table('infracciones',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('novedad_id', sa.Integer(), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('chofer_id', sa.Integer(), nullable=True),
        sa.Column('localidad_id', sa.Integer(), nullable=True),
        sa.Column('acta', sa.String(length=80), nullable=True),
        sa.Column('citacion', sa.String(length=80), nullable=True),
        sa.Column('causa', sa.String(length=80), nullable=True),
        sa.Column('tipo_pago_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['novedad_id'], ['novedades.id'], ),
        sa.ForeignKeyConstraint(['chofer_id'], ['choferes.id'], ),
        sa.ForeignKeyConstraint(['localidad_id'], ['localidades.id'], ),
        sa.ForeignKeyConstraint(['tipo_pago_id'], ['tipo_pago.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('novedad_id'),
    )
    op.create_index(op.f('ix_infracciones_id'), 'infracciones', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_infracciones_id'), table_name='infracciones')
    op.drop_table('infracciones')
    op.drop_index(op.f('ix_comodato_id'), table_name='comodato')
    op.drop_table('comodato')
    op.drop_index(op.f('ix_transferencias_id'), table_name='transferencias')
    op.drop_table('transferencias')
    op.drop_index(op.f('ix_robos_id'), table_name='robos')
    op.drop_table('robos')
    op.drop_index(op.f('ix_donaciones_id'), table_name='donaciones')
    op.drop_table('donaciones')
    op.drop_index(op.f('ix_accidentes_id'), table_name='accidentes')
    op.drop_table('accidentes')
    op.drop_index(op.f('ix_cambio_chasis_id'), table_name='cambio_chasis')
    op.drop_table('cambio_chasis')
    op.drop_index(op.f('ix_cambio_motor_id'), table_name='cambio_motor')
    op.drop_table('cambio_motor')
    op.drop_index(op.f('ix_bajas_id'), table_name='bajas')
    op.drop_table('bajas')
    op.drop_index(op.f('ix_vehiculo_dependencia_id'), table_name='vehiculo_dependencia')
    op.drop_table('vehiculo_dependencia')
    op.drop_index(op.f('ix_reparaciones_id'), table_name='reparaciones')
    op.drop_table('reparaciones')
    op.drop_index(op.f('ix_vtv_id'), table_name='vtv')
    op.drop_table('vtv')
    op.drop_index(op.f('ix_novedades_id'), table_name='novedades')
    op.drop_table('novedades')
    op.drop_index(op.f('ix_vehiculos_id'), table_name='vehiculos')
    op.drop_table('vehiculos')
    op.drop_index(op.f('ix_choferes_id'), table_name='choferes')
    op.drop_table('choferes')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_tipo_modelo_id'), table_name='tipo_modelo')
    op.drop_table('tipo_modelo')
    op.drop_index(op.f('ix_localidades_id'), table_name='localidades')
    op.drop_table('localidades')  
    op.drop_table('dependencia_dao')
    op.drop_index(op.f('ix_dependencias_id'), table_name='dependencias')
    op.drop_table('dependencias')
    op.drop_index(op.f('ix_talleres_id'), table_name='talleres')
    op.drop_table('talleres')
    op.drop_index(op.f('ix_tipo_vtv_resultado_id'), table_name='tipo_vtv_resultado')
    op.drop_table('tipo_vtv_resultado')
    op.drop_index(op.f('ix_tipo_vehiculo_id'), table_name='tipo_vehiculo')
    op.drop_table('tipo_vehiculo')
    op.drop_index(op.f('ix_tipo_tramite_dependencia_id'), table_name='tipo_tramite_dependencia')
    op.drop_table('tipo_tramite_dependencia')
    op.drop_index(op.f('ix_tipo_traccion_id'), table_name='tipo_traccion')
    op.drop_table('tipo_traccion')
    op.drop_index(op.f('ix_tipo_situacion_chofer_id'), table_name='tipo_situacion_chofer')
    op.drop_table('tipo_situacion_chofer')
    op.drop_index(op.f('ix_tipo_situacion_id'), table_name='tipo_situacion')
    op.drop_table('tipo_situacion')
    op.drop_index(op.f('ix_tipo_reparacion_estado_id'), table_name='tipo_reparacion_estado')
    op.drop_table('tipo_reparacion_estado')
    op.drop_index(op.f('ix_tipo_pago_id'), table_name='tipo_pago')
    op.drop_table('tipo_pago')
    op.drop_index(op.f('ix_tipo_novedad_id'), table_name='tipo_novedad')
    op.drop_table('tipo_novedad')
    op.drop_index(op.f('ix_tipo_motor_id'), table_name='tipo_motor')
    op.drop_table('tipo_motor')
    op.drop_index(op.f('ix_tipo_marca_id'), table_name='tipo_marca')
    op.drop_table('tipo_marca')
    op.drop_index(op.f('ix_tipo_documento_id'), table_name='tipo_documento')
    op.drop_table('tipo_documento')
    op.drop_index(op.f('ix_tipo_condicion_id'), table_name='tipo_condicion')
    op.drop_table('tipo_condicion')
    op.drop_index(op.f('ix_tipo_carroceria_id'), table_name='tipo_carroceria')
    op.drop_table('tipo_carroceria')
    op.drop_index(op.f('ix_tipo_cabina_id'), table_name='tipo_cabina')
    op.drop_table('tipo_cabina')
    op.drop_index(op.f('ix_tipo_aptitud_id'), table_name='tipo_aptitud')
    op.drop_table('tipo_aptitud')
    op.drop_index(op.f('ix_tipo_acto_id'), table_name='tipo_acto')
    op.drop_table('tipo_acto')
    op.drop_index(op.f('ix_provincias_id'), table_name='provincias')
    op.drop_table('provincias')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_table('roles')
