from utils.db_api.postgres import Database


class UserDatasDB:
    def __init__(self, db: Database):
        self.db = db

    async def add_user_datas(self, full_name, position, address, invertor_image, panel_model_image, photo_one,
                             photo_two, photo_three):
        sql = """INSERT INTO user_datas (full_name, position, address, invertor_image, panel_model_image, photo_one,
                             photo_two, photo_three) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)"""
        return await self.db.execute(sql, full_name, position, address, invertor_image, panel_model_image, photo_one,
                                     photo_two, photo_three, execute=True)
