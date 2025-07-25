from abc import ABC

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMINS


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()


class IsBotAdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        admin_ids_int = [int(id) for id in ADMINS]
        return int(message.from_user.id) in admin_ids_int
