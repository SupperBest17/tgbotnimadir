from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.inlinebutton import ikm
from loader import dp, bot
from states.personal import UserState


@dp.message_handler(commands="user")
async def get_info(message: types.Message):
    await message.answer(text="Foydalanuvchi to'liq ismini kiriting")
    await UserState.name.set()


@dp.message_handler(state=UserState.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer("Foydalanuvchini yoshini kiriting")
    # await UserState.age.set()
    await UserState.next()


@dp.message_handler(state=UserState.age)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await UserState.next()
    await message.answer("Foydalanuvchini raqamini kiriting")


@dp.message_handler(state=UserState.phone_number)
async def add_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    await UserState.next()
    await message.answer("Foydalanuvchini emailini kiriting")


@dp.message_handler(state=UserState.email)
async def add_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await UserState.next()
    await message.answer("Jinsingizni tanlang",
                         reply_markup=ikm)


@dp.message_handler(lambda message: message.text not in ["erkak", "ayol"], state=UserState.gender)
async def process_gender_invalid(message: types.Message):
    await message.reply("Noto'g'ri ma'lumot kiritildi!")
    await message.answer("Jinsingizni tanlang",
                         reply_markup=ikm)

@dp.callback_query_handler(lambda callback_query: callback_query.data in ["erkak", "ayol"], state=UserState.gender)
async def process_gender(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback_query.data)
    # await bot.answer_callback_query(callback_query.id)

    await UserState.next()
    await callback_query.message.answer("Foydalanuvchi rasmini yuboring")

@dp.message_handler(state=UserState.photo, content_types=['photo'])
async def add_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await state.finish()
    await message.answer("Ma'lumotingiz saqlandi")

    await message.answer_photo(photo=data['photo'],
                               caption=f"Foydalanuvchini ismi {data['name']},\n"
                         f"Foydalanauvchining yoshi {data['age']},\n"
                         f"Foydalanuvchining raqami {data['phone_number']},\n"
                         f"email manzili - {data['email']}\n"
                         f"Jinsi - {data['gender']}")



