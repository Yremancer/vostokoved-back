from fastapi import APIRouter
from fastapi_restful.cbv import cbv


dialog_router = APIRouter()


@cbv(dialog_router)
class DialogRouter:

    def __init__(self, session_id: str | None):
        self.session_id = session_id


    # Блок с пользователями
    @dialog_router.post('/user', summary="Создание нового пользователя") 
    async def create_new_user(self) -> str:
        pass
    

    # Блок с чатами
    @dialog_router.post('/chat', summary="Создание нового чата") 
    async def create_new_chat(self) -> str:
        pass

    @dialog_router.get('/chat', summary="Получение чатов пользователя") 
    async def create_new_chat(self) -> str:
        pass
    
    
    # Блок с сообщениями
    @dialog_router.post('/message', summary="Отправка сообщения") 
    async def send_message(self, chat_id: str | None):
        pass
    
