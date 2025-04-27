import asyncio
from run import initdb  # adjust path based on where you placed db.py

if __name__ == "__main__":
    asyncio.run(initdb())
