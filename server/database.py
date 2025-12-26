import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel

# Replace with your Ubuntu Postgres credentials
# Format: postgresql+asyncpg://user:password@host:port/dbname
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://myroot:1234@localhost/bidmanager")

# Create Async Engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Function to provide an async session to your routes
async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

# Helper to create tables (useful for dev; use Alembic for production)
async def init_db():
    async with engine.begin() as conn:
        # Import models here to ensure they are registered with SQLModel.metadata
        from .models.user import User 
        await conn.run_sync(SQLModel.metadata.create_all)
