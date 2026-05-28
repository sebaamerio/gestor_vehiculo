from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..repositories import user_repository
from ..core.security import verify_password, create_access_token, create_refresh_token, decode_token
from ..schemas.auth_schema import LoginRequest, TokenResponse, TokenPayload


def _build_token_payload(user) -> dict:
    return {
        "sub": user.username,
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "nombre": user.nombre,
        "role": user.role.nombre,
    }


def login(db: Session, data: LoginRequest) -> tuple[str, str]:
    user = user_repository.get_by_username(db, data.username)

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
        )

    if not user.activo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo",
        )

    payload = _build_token_payload(user)
    access_token = create_access_token(payload)
    refresh_token = create_refresh_token({"sub": user.username, "user_id": user.id})
    return access_token, refresh_token


def refresh_access_token(db: Session, refresh_token: str) -> str:
    payload = decode_token(refresh_token)

    if not payload or payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token inválido o expirado",
        )

    user_id: int = payload.get("user_id")
    user = user_repository.get_by_id(db, user_id)

    if not user or not user.activo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado o inactivo",
        )

    return create_access_token(_build_token_payload(user))


def get_me(db: Session, user_id: int):
    user = user_repository.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user
