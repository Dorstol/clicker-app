from typing import Optional

from core.models import User
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.schemas.user import UserUpdate


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
