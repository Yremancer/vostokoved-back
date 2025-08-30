from fastapi import APIRouter, Depends, Header
from fastapi_restful.cbv import cbv
from sqlalchemy.ext.asyncio import AsyncSession
from ..global_funcs import exception_handler
from .dialog_schemas import Answer, ChatSchema, EditMessageSchema, MessageSchema, SendMessageSchema
from .dialog_service import DialogService
from database.database import get_session_obj
from database.models import PlatformTypes

dialog_router = APIRouter()


@cbv(dialog_router)
class DialogRouter:

    def __init__(
        self,
        session_id: str | None = Header(None),
        db_session: AsyncSession = Depends(get_session_obj),
    ):
        self.session_id = session_id
        self.dialog_service = DialogService(db_session=db_session)

    # Блок с пользователями
    @dialog_router.post("/user", summary="Создание нового пользователя")
    @exception_handler
    async def create_new_user(self) -> str:
        return await self.dialog_service.create_new_user(platform_type=PlatformTypes.web)

    # Блок с чатами (Изпользуется вебом)
    @dialog_router.post("/chat", summary="Создание нового чата")
    @exception_handler
    async def create_new_chat(self) -> int:
        return await self.dialog_service.create_new_chat(session_id = self.session_id)

    @dialog_router.get("/chat", summary="Получение чатов пользователя")
    @exception_handler
    async def get_chats(self) -> list[ChatSchema]:
        return await self.dialog_service.get_user_chats(session_id = self.session_id)
    
    @dialog_router.post("/chat-delete", summary="Получение чатов пользователя")
    @exception_handler
    async def delete_chat(self, chat_id: int):
        return await self.dialog_service.delete_chat(chat_id = chat_id)

    # Блок с сообщениями
    @dialog_router.post("/message", summary="Отправка сообщения")
    @exception_handler
    async def send_message(self, send_message: SendMessageSchema) -> Answer:
        return await self.dialog_service.send_message(text=send_message.text, chat_id = send_message.chat_id)

    @dialog_router.get("/message", summary="Получение сообщений чата")
    @exception_handler
    async def get_messages(self, chat_id: int) -> list[MessageSchema]:
        return await self.dialog_service.get_chat_messages(chat_id = chat_id)
    