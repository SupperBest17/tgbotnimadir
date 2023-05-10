from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

rkm = ReplyKeyboardMarkup()
button = KeyboardButton(text="/start")
button1 = KeyboardButton(text="/help")
button2 = KeyboardButton(text="user")
rkm.add(button, button1, button2)