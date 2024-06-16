from pydantic import BaseModel, ConfigDict


class EnemyBase(BaseModel):
    pass


class EnemyRead(EnemyBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
    name: int
    max_hp: int
    current_hp: int
    gold_reward: int
    is_dead: bool

