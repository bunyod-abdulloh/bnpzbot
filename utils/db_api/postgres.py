from typing import Union

import asyncpg
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args, fetch=False, fetchval=False, fetchrow=False, execute=False):
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)  # *args bilan argumentlar yuboriladi
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)  # To'g'ri uzatilgan argumentlar
        return result

    async def create_tables(self):
        queries = [
            """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    telegram_id BIGINT NOT NULL UNIQUE                                                    
            );
            """,
            """
                CREATE TABLE IF NOT EXISTS admins (
                    id SERIAL PRIMARY KEY,
                    status BOOLEAN DEFAULT FALSE                                
                );
            """
        ]
        for query in queries:
            await self.execute(query, execute=True)
