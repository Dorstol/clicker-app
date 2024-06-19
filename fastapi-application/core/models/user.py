from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class User(IntIdPkMixin, Base):
    tg_id: Mapped[int] = mapped_column(
        BigInteger,
    )
    username: Mapped[str] = mapped_column(
        unique=True,
    )
    # photo
    attack_power: Mapped[int] = mapped_column(
        server_default="1",
    )
    gold: Mapped[int] = mapped_column(
        server_default="650",
    )
    max_energy: Mapped[int] = mapped_column(
        server_default="2000",
    )
    current_energy: Mapped[int] = mapped_column(
        server_default="2000",
    )

    enemy: Mapped["Enemy"] = relationship(
        back_populates="user",
        secondary="users_enemy",
    )


class UsersEnemy(IntIdPkMixin, Base):
    __tablename__ = "users_enemy"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    enemy_id: Mapped[int] = mapped_column(
        ForeignKey("enemies.id", ondelete="CASCADE"),
        primary_key=True,
    )
