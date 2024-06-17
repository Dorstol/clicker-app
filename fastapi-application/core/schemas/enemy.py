from pydantic import BaseModel, ConfigDict


class EnemyBase(BaseModel):
    name: str
    max_hp: int
    current_hp: int
    gold_reward: int
    is_dead: bool


class EnemyRead(EnemyBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
    )
