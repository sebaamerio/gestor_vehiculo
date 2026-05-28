from sqlalchemy.orm import Session
from ..models.user_model import User
from ..schemas.user_schema import UserCreate, UserUpdate
from ..core.security import hash_password


def get_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


def get_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def get_all(db: Session) -> list[User]:
    return db.query(User).all()


def create(db: Session, data: UserCreate) -> User:
    user = User(
        nombre=data.nombre,
        username=data.username,
        email=data.email,
        password_hash=hash_password(data.password),
        activo=data.activo,
        role_id=data.role_id,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update(db: Session, user: User, data: UserUpdate) -> User:
    for field, value in data.model_dump(exclude_unset=True).items():
        if field == "password":
            user.password_hash = hash_password(value)
        else:
            setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, user: User) -> User:
    db.delete(user)
    db.commit()
    return user
