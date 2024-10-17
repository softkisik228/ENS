from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Boolean, Integer, Column, ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

from .mixins.id_int_pk import IdIntPkMixin


DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    pass


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):

    username: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=False
    )


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)