from utils.db_api.postgres import Database


class AdminDB:
    def __init__(self, db: Database):
        self.db = db

    # ====================== ADMINS ======================
    async def add_send_status(self):
        sql = "INSERT INTO admins (status) VALUES (FALSE)"
        await self.db.execute(sql, execute=True)

    async def update_status_true(self):
        sql = "UPDATE admins SET status = TRUE"
        return await self.db.execute(sql, execute=True)

    async def update_status_false(self):
        sql = "UPDATE admins SET status = FALSE"
        return await self.db.execute(sql, execute=True)

    async def get_send_status(self):
        sql = "SELECT status FROM admins"
        return await self.db.execute(sql, fetchval=True)

    async def drop_table_admins(self):
        sql = "DROP TABLE admins"
        return await self.db.execute(sql, execute=True)
