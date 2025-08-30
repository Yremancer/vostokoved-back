from pydantic import BaseModel, Field
from database.models import Senders


class Answer(BaseModel):
    user_message_id: int = Field(...)
    model_message: str = Field(...)       


class MessageSchema(BaseModel):
    id: int = Field(...)
    text: str = Field(...)
    sender: Senders = Field(...)

class ChatSchema(BaseModel):
    id: int = Field(...)
    name: str = Field(...)