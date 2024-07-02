import time
from typing import Annotated

from utils import verify_hash
from core.models import db_helper
from core.schemas.user import (
    UserRead,
    UserUpdate,
)
from crud import users as users_crud
from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["Users"])


@router.get("/login", response_model=UserRead)
async def login(request: Request):
    """
    Handle user login via Telegram WebApp.

    This endpoint verifies the login data received from the Telegram WebApp,
    checks if the data is not corrupted and if the authentication date is valid.
    If the user does not exist in the database, it creates a new user entry.

    Args:
        request (Request): The FastAPI request object containing the login data.

    Returns:
        UserRead: The user information in the form of a UserRead schema.
        dict: An error message if the data is corrupted or the authentication date is expired.
    """
    body = await request.json()
    auth_date = body.get("auth_date")
    username = body.get("username")
    telegram_id = body.get("id")

    calculated_hash = await verify_hash(request)

    if hash != calculated_hash:
        return {"error": "Data is corrupted"}

    if time.time() - int(auth_date) > 86400:
        return {"error": "Auth date expired"}

    user = await users_crud.set_user(tg_id=telegram_id, username=username)
    return user


@router.get("/user", response_model=UserRead)
async def get_user(
    user_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    """
    Retrieve a user by their ID.

    This endpoint retrieves a user from the database using their unique user ID.
    If the user is not found, a 404 HTTPException is raised.

    Args:
        user_id (int): The unique ID of the user to retrieve.
        session (AsyncSession): The SQLAlchemy session dependency.

    Returns:
        UserRead: The user information in the form of a UserRead schema.
    """
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
    """
    Update user information.

    This endpoint updates the details of an existing user in the database.
    The user is identified by their unique user ID, and the new data is provided
    in the form of a UserUpdate schema.

    Args:
        user_id (int): The unique ID of the user to update.
        user_update (UserUpdate): The new data to update the user with.
        session (AsyncSession): The SQLAlchemy session dependency.

    Returns:
        UserRead: The updated user information in the form of a UserRead schema.
    """
    user = await users_crud.update_user(
        user_id=user_id,
        user_update=user_update,
        session=session,
    )
    return user
