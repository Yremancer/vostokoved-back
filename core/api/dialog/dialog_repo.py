from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Chat, Message, PlatformTypes, User


class DialogRepository:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
    
    async def create_new_user(self, user_data: dict):
        new_user = User(**user_data)
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user.session_id
    
    async def get_user(self, session_id: str):
        user =( await self.db_session.execute(select(User).where(User.session_id==session_id))).scalar()
        if user:
            return user.id
        return None
        
    async def create_new_chat(self, chat_data: dict):
        new_chat = Chat(**chat_data)
        self.db_session.add(new_chat)
        await self.db_session.flush()
        return new_chat.id
    
    async def get_chats(self, user_id: int):
        chats = (await self.db_session.execute(select(Chat).where(Chat.user_id==user_id))).scalars().all()

        if chats:
            return chats
        
        return None
    
    async def delete_chat(self, chat_id: int):
        await self.db_session.execute(delete(Chat).where(Chat.id==chat_id))

    async def get_messages(self, chat_id: int):

        messages = (await self.db_session.execute(select(Message).where(Message.chat_id==chat_id))).scalars().all()

        if messages:
            return messages
        
        return None
    
    async def create_new_message(self, message_data: dict):
        new_message = Message(**message_data)
        self.db_session.add(new_message)
        await self.db_session.flush()
        return new_message.id
    
    async def edit_message(self, message_id: int, text: str):
        message = (await self.db_session.execute(select(Message).where(Message.id==message_id))).scalar()
        message.text = text
        await self.db_session.refresh()
        
        
