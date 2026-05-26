from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone



db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    gender: Mapped[str] = mapped_column(String(50))
    eye_color: Mapped[str] = mapped_column(String(50))
    hair_color: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    climate: Mapped[str] = mapped_column(String(120))
    terrain: Mapped[str] = mapped_column(String(120))
    population: Mapped[str] = mapped_column(String(120))
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    character_id: Mapped[str] = mapped_column(ForeignKey("character.id"), nullable=True)
    planet_id: Mapped[str] = mapped_column(ForeignKey("planet.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

    user = relationship("User")
    character = relationship("Character")
    planet = relationship("Planet")
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
