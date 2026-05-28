from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    nombre: str
    username: str
    email: EmailStr
    activo: bool = True


class UserCreate(UserBase):
    password: str
    role_id: int


class UserUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    activo: Optional[bool] = None
    role_id: Optional[int] = None
    password: Optional[str] = None


class RoleOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nombre: str


class UserOut(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    role: RoleOut
    created_at: datetime
    updated_at: datetime
