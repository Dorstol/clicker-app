from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class Enemy(IntIdPkMixin, Base):
    __tablename__ = "enemies"

    name: Mapped[str] = mapped_column(unique=True)
    # image
    # icon
    level: Mapped[int]
    max_hp: Mapped[int]
    current_hp: Mapped[int]
    gold_reward: Mapped[int]
    is_dead: Mapped[bool] = mapped_column(default=False)

    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    user = relationship("User", back_populates="enemy")