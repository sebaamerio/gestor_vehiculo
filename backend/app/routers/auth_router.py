from fastapi import APIRouter, Depends, Response, Cookie
from sqlalchemy.orm import Session
from typing import Optional
from ..core.database import get_db
from ..core.deps import get_current_user
from ..core.config import settings
from ..services import auth_service
from ..schemas.auth_schema import LoginRequest, TokenResponse
from ..schemas.user_schema import UserOut

router = APIRouter(prefix="/auth", tags=["Auth"])

_REFRESH_COOKIE = "refresh_token"
_COOKIE_MAX_AGE = settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60


def _set_refresh_cookie(response: Response, token: str) -> None:
    response.set_cookie(
        key=_REFRESH_COOKIE,
        value=token,
        httponly=True,
        secure=settings.ENV == "prod",
        samesite="lax",
        max_age=_COOKIE_MAX_AGE,
        path="/auth/refresh",
    )


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, response: Response, db: Session = Depends(get_db)):
    access_token, refresh_token = auth_service.login(db, data)
    _set_refresh_cookie(response, refresh_token)
    return TokenResponse(access_token=access_token)


@router.post("/refresh", response_model=TokenResponse)
def refresh(
    response: Response,
    db: Session = Depends(get_db),
    refresh_token: Optional[str] = Cookie(default=None, alias=_REFRESH_COOKIE),
):
    if not refresh_token:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token no encontrado",
        )
    access_token = auth_service.refresh_access_token(db, refresh_token)
    return TokenResponse(access_token=access_token)


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key=_REFRESH_COOKIE, path="/auth/refresh")
    return {"detail": "Sesión cerrada correctamente"}


@router.get("/me", response_model=UserOut)
def me(current_user=Depends(get_current_user)):
    return current_user
