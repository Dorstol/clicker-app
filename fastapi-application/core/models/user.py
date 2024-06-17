from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
    # photo
    attack_power: Mapped[int] = mapped_column(server_default="1")
    gold: Mapped[int] = mapped_column(server_default="650")
    max_energy: Mapped[int] = mapped_column(server_default="2000")
    current_energy: Mapped[int] = mapped_column(server_default="2000")

    enemy_id = Column(Integer, ForeignKey('enemies.id'), unique=True, server_default="1")
    enemy = relationship("Enemy", back_populates="users")
