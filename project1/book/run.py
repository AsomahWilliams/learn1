from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlalchemy import text
from config import Config
import asyncio
# ✅ Correct async MySQL engine setup
engine = create_async_engine(
    url=Config.DATABASE_URL,  # must be in async form!
    echo=True
)

async def initdb():
    """Try connecting to the MySQL DB and test it."""
    try:
        async with engine.begin() as conn:
            # Run a simple query to check the connection
            result = await conn.execute(text("SELECT 'Connection Successful'"))
            print(result.scalar())

    except Exception as e:
        print("❌ Error:", e)
    finally:
        # Ensure the engine is properly closed
        await engine.dispose()
        print("🔌 Connection closed.")

# Properly manage the asyncio event loop
if __name__ == "__main__":
    asyncio.run(initdb())