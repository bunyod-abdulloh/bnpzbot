import asyncio
from itertools import islice


def chunk_dict(data: dict, size: int):
    it = iter(data.items())
    while chunk := list(islice(it, size)):
        yield dict(chunk)


# --- 2. Asosiy ishlovchi funksiya
async def process_users_in_batches(users: dict, db, batch_size: int = 100):
    for batch in chunk_dict(users, batch_size):
        tasks = [
            db.add_user(telegram_id=int(telegram_id))
            for _, telegram_id in batch.items()
        ]

        try:
            await asyncio.gather(*tasks)
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")  # logga yozish tavsiya etiladi

        await asyncio.sleep(1)  # Har batchdan keyin dam olish


