from pydantic import BaseModel
from pydantic import ConfigDict

from .enemy import EnemyRead


class UserBase(BaseModel):
    username: str


class UserUpdate(UserBase):
    attack_power: int
    gold: int
    max_energy: int
    current_energy: int


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
