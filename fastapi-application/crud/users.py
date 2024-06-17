from core.models import User
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload


async def get_user(
    user_id: int,
    session: AsyncSession,
) -> User:
    try:
        stmt = select(User).where(User.id == user_id).options(joinedload(User.enemy))
        result = await session.execute(stmt)
        return result.scalar_one()
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="DOES_NOT_EXIST",
        )
