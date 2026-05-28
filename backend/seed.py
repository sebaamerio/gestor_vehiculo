"""
Script de seed: crea roles y usuarios iniciales.
Ejecutar desde backend/:
    python seed.py
"""
from app.core.database import SessionLocal
from app.models.role_model import Role
from app.models.user_model import User
from app.core.security import hash_password


ROLES = [
    {"nombre": "admin", "descripcion": "Administrador del sistema"},
    {"nombre": "user",  "descripcion": "Usuario estándar (solo lectura)"},
]

USERS = [
    {
        "nombre":   "Administrador",
        "username": "admin",
        "email":    "admin@okauto.gov.ar",
        "password": "Admin123!",
        "role":     "admin",
    },
    {
        "nombre":   "Usuario",
        "username": "user",
        "email":    "user@okauto.gov.ar",
        "password": "User123!",
        "role":     "user",
    },
]


def seed():
    db = SessionLocal()
    try:
        # ── Roles ────────────────────────────────────────────────────────────
        role_map = {}
        for r in ROLES:
            existing = db.query(Role).filter(Role.nombre == r["nombre"]).first()
            if existing:
                print(f"  [skip] rol '{r['nombre']}' ya existe")
                role_map[r["nombre"]] = existing
            else:
                role = Role(**r)
                db.add(role)
                db.flush()
                role_map[r["nombre"]] = role
                print(f"  [ok]   rol '{r['nombre']}' creado")

        db.commit()

        # ── Usuarios ─────────────────────────────────────────────────────────
        for u in USERS:
            existing = db.query(User).filter(User.username == u["username"]).first()
            if existing:
                print(f"  [skip] usuario '{u['username']}' ya existe")
                continue

            user = User(
                nombre=u["nombre"],
                username=u["username"],
                email=u["email"],
                password_hash=hash_password(u["password"]),
                activo=True,
                role_id=role_map[u["role"]].id,
            )
            db.add(user)
            print(f"  [ok]   usuario '{u['username']}' creado (rol: {u['role']})")

        db.commit()
        print("\nSeed completado.")

    except Exception as e:
        db.rollback()
        print(f"\nError durante el seed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
