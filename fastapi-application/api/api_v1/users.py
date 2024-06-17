from typing import Annotated

from core.models import db_helper
from core.schemas.user import (
    UserRead,
)
from crud import users as users_crud
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["Users"])


@router.get("", response_model=UserRead)
async def get_user(
    user_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    user = await users_crud.get_user(
        user_id=user_id,
        session=session,
    )
    return user
