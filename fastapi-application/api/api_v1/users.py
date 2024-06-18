from typing import Annotated

from core.models import db_helper, User
from core.schemas.user import (
    UserRead,
    UserUpdate,
)
from crud import users as users_crud
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["Users"])


@router.get("/user", response_model=UserRead)
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


@router.patch("/user/update", response_model=UserRead)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    user = await users_crud.update_user(
        user_id=user_id,
        user_update=user_update,
        session=session,
    )
    return user
