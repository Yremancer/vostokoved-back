from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


# DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#Url для sqlite базы
DATABASE_URL = "sqlite+aiosqlite:///database/dventor.db"
base = declarative_base()


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_session_obj() -> AsyncGenerator[AsyncSession, None]:
    session = async_session_maker()
    async with session.begin():
        yield session
    await session.close()
