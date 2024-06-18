from pydantic import BaseModel
from pydantic import ConfigDict

from .enemy import EnemyRead


class UserBase(BaseModel):
    username: str


class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    attack_power: int
    gold: int
    max_energy: int
    current_energy: int
    enemy: EnemyRead


class UserUpdate(BaseModel):
    attack_power: int | None = None
    gold: int | None = None
    max_energy: int | None = None
    current_energy: int | None = None
