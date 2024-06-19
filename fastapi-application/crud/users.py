from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import User
from core.schemas.user import UserUpdate
from core.models import db_helper


async def get_user(
        user_id: int,
        session: AsyncSession,
) -> Optional[User]:
    try:
        stmt = select(User).where(User.id == user_id).options(joinedload(User.enemy))
        result = await session.execute(stmt)
        return result.scalar_one()
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="DOES_NOT_EXIST",
        )


async def update_user(
        user_id: int,
        user_update: UserUpdate,
        session: AsyncSession,
) -> Optional[User]:
    user = await get_user(user_id, session)
    try:
        for name, value in user_update.model_dump(exclude_unset=True).items():
            setattr(user, name, value)
            await session.commit()
            return user
    except NoResultFound:
        pass


async def set_user(tg_id: int, username: str):
    async with db_helper.session_getter() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, username=username))
            await session.commit()
