from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_main_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
admin_main_buttons.row("😎 Foydalanuvchilar soni")
admin_main_buttons.row("✅ Oddiy post yuborish", "🎞 Mediagroup post yuborish")
admin_main_buttons.row("👤 Export users")
admin_main_buttons.row(KeyboardButton("🏡 Bosh sahifa"))
