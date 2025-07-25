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
                CREATE TABLE IF NOT EXISTS link_table (
                    id SERIAL PRIMARY KEY,
                    inviter BIGINT NOT NULL,
                    new_member BIGINT NOT NULL UNIQUE,
                    invite_count INTEGER DEFAULT 0,
                    created_at DATE DEFAULT CURRENT_DATE            
                );
            """,
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

    # ====================== LINK_TABLE ======================
    async def add_members(self, inviter, new_member, invite_count):
        sql = "INSERT INTO link_table (inviter, new_member, invite_count) VALUES ($1, $2, $3) returning id"
        return await self.execute(sql, inviter, new_member, invite_count, fetchrow=True)

    async def count_members(self, inviter):
        sql = "SELECT COUNT(*) FROM link_table WHERE inviter = $1"
        return await self.execute(sql, inviter, fetchval=True)

    async def delete_old_links(self):
        sql = "DELETE FROM link_table WHERE created_at != CURRENT_DATE"
        return await self.execute(sql, execute=True)

    async def delete_inviter(self, inviter):
        sql = "DELETE FROM link_table WHERE inviter = $1"
        return await self.execute(sql, inviter, execute=True)

    async def drop_table_links(self):
        sql = "DROP TABLE link_table"
        return await self.execute(sql, execute=True)

    # ====================== USERS ======================
    async def add_user(self, telegram_id):
        sql = "INSERT INTO users (telegram_id) VALUES ($1) ON CONFLICT (telegram_id) DO NOTHING"
        await self.execute(sql, telegram_id, execute=True)

    async def select_user(self, telegram_id):
        sql = "SELECT * FROM users WHERE telegram_id = $1"
        return await self.execute(sql, telegram_id, fetchval=True)

    async def select_all_users(self):
        sql = "SELECT telegram_id FROM users "
        return await self.execute(sql, fetch=True)

    async def select_users_offset(self, offset: int = 0, limit: int = 1000):
        sql = "SELECT telegram_id FROM users ORDER BY id LIMIT $1 OFFSET $2"
        return await self.execute(sql, limit, offset, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users"
        return await self.execute(sql, fetchval=True)

    async def delete_user(self, telegram_id):
        sql = "DELETE FROM users WHERE telegram_id = $1"
        return await self.execute(sql, telegram_id, execute=True)

    async def drop_table_users(self):
        sql = "DROP TABLE users"
        return await self.execute(sql, execute=True)

    # ====================== ADMINS ======================
    async def add_send_status(self):
        sql = "INSERT INTO admins (status) VALUES (FALSE)"
        await self.execute(sql, execute=True)

    async def update_status_true(self):
        sql = "UPDATE admins SET status = TRUE"
        return await self.execute(sql, execute=True)

    async def update_status_false(self):
        sql = "UPDATE admins SET status = FALSE"
        return await self.execute(sql, execute=True)

    async def get_send_status(self):
        sql = "SELECT status FROM admins"
        return await self.execute(sql, fetchval=True)

    async def drop_table_admins(self):
        sql = "DROP TABLE admins"
        return await self.execute(sql, execute=True)
