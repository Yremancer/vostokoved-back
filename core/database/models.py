from datetime import date
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, Enum, String
from database.database import base
from enum import Enum as PyEnum


class PlatformTypes(PyEnum):
    web = "web"
    telegram = "telegram"
    max = "max"


class Senders(PyEnum):
    user = "user"
    model = "model"


class User(base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True)
    platform_type: PlatformTypes = Column(Enum(PlatformTypes), nullable=False)
    session_id: str = Column(String, unique=True, nullable=False)

    telegram_id: int = Column(String, unique=True, nullable=True)
    create_date: date = Column(TIMESTAMP, nullable=False)


class Chat(base):
    __tablename__ = "chats"
    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(ForeignKey(column="users.id", ondelete="CASCADE"), nullable=False)

    name: str = Column(String, nullable=False)
    create_date: date = Column(TIMESTAMP, nullable=False)


class Message(base):
    __tablename__ = "messages"
    id: int = Column(Integer, primary_key=True)
    chat_id: int = Column(ForeignKey(column="chats.id", ondelete="CASCADE"), nullable=False)

    text: str = Column(String, nullable=False)
    sender: Senders = Column(Enum(Senders), nullable=False)
    create_date: date = Column(TIMESTAMP, nullable=False)
