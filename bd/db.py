from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import config


engine = create_async_engine(
    config.database_dsn,
    echo=True
)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


async def get_session():
    return async_session
# async def get_session():
#     async with async_session() as session:
#         yield session
