from pydantic import BaseModel, Field
from database.models import Senders


class MessageSchema(BaseModel):
    text: str = Field(...)
    sender: Senders = Field(...)

class ChatSchema(BaseModel):
    messages: list[MessageSchema] = Field(...)