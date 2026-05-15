import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from backend.src.models.vehicle import Base


async def init_db():
    engine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost:5432/haim_mas")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(init_db())