from typing import Optional
from fastapi import Depends, Header, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..global_funcs import exception_handler
from database.database import get_session_obj
from database.models import User



# Написал для универсального получения сессии независимо от платформы, но пояивлись сомнения в надобности, ведь телеграм все равно будет обрабатываться иначе
@exception_handler
async def get_session_id(
    request: Request,
    session_id: Optional[str] = Header(None),
    db_session: AsyncSession = Depends(get_session_obj),
) -> Optional[str]:

    body = await request.json()

    # Попытка получить session_id из заголовка session_id (для веб-клиентов)
    if session_id:
        result = await db_session.execute(
            select(User).where(User.session_id == session_id)
        )
        user = result.scalar()
        if user:
            return session_id

    # Попытка получить session_id из тела запроса (для Telegram)
    if "message" in body and "from" in body["message"]:
        telegram_id = str(body["message"]["from"]["id"])
        result = await db_session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar()
        if user:
            return user.session_id

    return None
