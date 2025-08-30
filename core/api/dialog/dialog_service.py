from sqlalchemy.ext.asyncio import AsyncSession
from config import LLM_ON
from .dialog_funcs import get_response
from database.models import PlatformTypes
from .dialog_repo import DialogRepository
from uuid import uuid4
from database.models import Senders
from datetime import datetime


class DialogService:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.dialog_repository = DialogRepository(db_session=db_session)

    # Тут основные действия при какой то отправке сообщения пользователем
    async def send_message(self, text: str, chat_id: int):

        user_message_data = {
            "chat_id": chat_id,
            "text": text,
            "sender": Senders.user,
            "create_date": datetime.utcnow(),
        }

        user_message_id = await self.dialog_repository.create_new_message(
            message_data=user_message_data
        )

        # Какой либо запрос к llm, но пока так

        if LLM_ON:
            response = await get_response(query=text)

            model_message_data = {
                "chat_id": chat_id,
                "text": response["answer"],
                "sender": Senders.model,
                "create_date": datetime.utcnow(),
            }
        else:
            model_message_data = {
                "chat_id": chat_id,
                "text": "Тестовый ответ",
                "sender": Senders.model,
                "create_date": datetime.utcnow(),
            }

        model_message_id = await self.dialog_repository.create_new_message(
            message_data=model_message_data
        )

        return {
            "user_message_id": user_message_id,
            "model_message_id": model_message_id,
            "model_message": model_message_data["text"],
        }

    async def create_new_user(
        self, platform_type: PlatformTypes, telegram_id: int | None = None
    ) -> str:
        session_id = str(uuid4())

        user_data = {
            "session_id": session_id,
            "platform_type": platform_type,
            "telegram_id": telegram_id,
            "create_date": datetime.utcnow(),
        }

        return await self.dialog_repository.create_new_user(user_data=user_data)

    async def create_new_chat(self, session_id: int):
        user_id = await self.dialog_repository.get_user(session_id=session_id)

        if not user_id:
            raise

        chat_data = {
            "user_id": user_id,
            "name": "Новый чат",
            "create_date": datetime.utcnow(),
        }

        return await self.dialog_repository.create_new_chat(chat_data=chat_data)

    async def get_user_chats(self, session_id: int):
        user_id = await self.dialog_repository.get_user(session_id=session_id)

        if not user_id:
            raise

        chats = await self.dialog_repository.get_chats(user_id=user_id)

        if not chats:
            return []

        return chats

    async def delete_chat(self, chat_id: int):
        await self.dialog_repository.delete_chat(chat_id=chat_id)

    async def get_chat_messages(self, chat_id: int):
        messages = await self.dialog_repository.get_messages(chat_id=chat_id)

        if not messages:
            raise

        return []

    async def edit_message(self, message_id: int, text: str):
        await self.dialog_repository.edit_message(message_id=message_id, text=text)
