from utils.db_api.postgres import Database


class UserDB:
    def __init__(self, db: Database):
        self.db = db

    # ====================== USERS ======================
    async def add_user(self, telegram_id):
        sql = "INSERT INTO users (telegram_id) VALUES ($1) ON CONFLICT (telegram_id) DO NOTHING"
        await self.db.execute(sql, telegram_id, execute=True)

    async def select_user(self, telegram_id):
        sql = "SELECT * FROM users WHERE telegram_id = $1"
        return await self.db.execute(sql, telegram_id, fetchval=True)

    async def select_all_users(self):
        sql = "SELECT telegram_id FROM users "
        return await self.db.execute(sql, fetch=True)

    async def select_users_offset(self, offset: int = 0, limit: int = 1000):
        sql = "SELECT telegram_id FROM users ORDER BY id LIMIT $1 OFFSET $2"
        return await self.db.execute(sql, limit, offset, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users"
        return await self.db.execute(sql, fetchval=True)

    async def delete_user(self, telegram_id):
        sql = "DELETE FROM users WHERE telegram_id = $1"
        return await self.db.execute(sql, telegram_id, execute=True)

    async def drop_table_users(self):
        sql = "DROP TABLE users"
        return await self.db.execute(sql, execute=True)
