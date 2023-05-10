from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikm = InlineKeyboardMarkup(row_width=2)
inline = InlineKeyboardButton(text="Erkak", callback_data="erkak")
inline1 = InlineKeyboardButton(text="Ayol", callback_data="ayol")
ikm.add(inline, inline1)

