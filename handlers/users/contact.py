from aiogram import types

from loader import dp, bot


@dp.message_handler(commands='contact')
async def send_contact(message: types.Message):
    await bot.send_contact(chat_id=message.chat.id,
                           phone_number="+998912011238",
                           first_name="Akbarjon Sheraliyev")
