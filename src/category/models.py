from typing import AsyncGenerator

from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

metadata = MetaData()

Category = Table(
    "Category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("slug", String, nullable=False),
)

# DATABASE_URL = "sqlite+aiosqlite:///../../database.db"
DATABASE_URL = "postgresql+asyncpg://postgres:12345@localhost:5432/postgres"

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
