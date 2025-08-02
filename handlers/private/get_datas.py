from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from loader import dp
from states.user import UserGetDatas


@dp.message_handler(F.text == "Ro'yxatdan o'tish", state="*")
async def handle_register_main(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text="Ism sharifingizni kiriting"
    )
    await UserGetDatas.FULLNAME.set()


@dp.message_handler(state=UserGetDatas.FULLNAME, content_types=types.ContentType.TEXT)
async def handle_get_fullname(message: types.Message, state: FSMContext):
    await state.update_data(
        fullname=message.text.strip()
    )
    await message.answer(
        text="Lavozimingizni kiriting"
    )
    await UserGetDatas.POSITION.set()


@dp.message_handler(state=UserGetDatas.POSITION, content_types=types.ContentType.TEXT)
async def handle_position(message: types.Message, state: FSMContext):
    await state.update_data(
        position=message.text.strip()
    )
    await message.answer(
        text="Quyosh panel o'rnatilgan manzilni kiriting\n\n<b>Namuna:</b>"
    )
    await UserGetDatas.ADDRESS.set()


@dp.message_handler(state=UserGetDatas.ADDRESS, content_types=types.ContentType.TEXT)
async def handle_address(message: types.Message, state: FSMContext):
    await state.update_data(
        address=message.text.strip()
    )
    await message.answer(
        text="Invertor modeli rasmini yuboring"
    )
    await UserGetDatas.INVERTOR.set()


@dp.message_handler(state=UserGetDatas.INVERTOR, content_types=types.ContentType.PHOTO)
async def handle_invertor_image(message: types.Message, state: FSMContext):
    await state.update_data(
        invertor_image=message.photo[-1].file_id
    )
    await message.answer(
        text="Panel modeli rasmini yuboring"
    )
    await UserGetDatas.PANEL.set()


@dp.message_handler(state=UserGetDatas.PANEL, content_types=types.ContentType.PHOTO)
async def handle_panel_model_image(message: types.Message, state: FSMContext):
    await state.update_data(
        panel_model_image=message.photo[-1].file_id
    )
    await message.answer_photo(
        photo="AgACAgIAAxkBAAN7aI4IuVZ9S8v7_H48VSP0Klzdn2UAArD0MRv8OnFIIji2aCjc5E4BAAMCAANtAAM2BA",
        caption="Soliqdan olingan 1 - hujjat rasmini yuboring"
    )
    await UserGetDatas.PHOTO_ONE.set()


@dp.message_handler(state=UserGetDatas.PHOTO_ONE, content_types=types.ContentType.PHOTO)
async def handle_photo_one(message: types.Message, state: FSMContext):
    await state.update_data(
        photo_one=message.photo[-1].file_id
    )
    await message.answer_photo(
        photo="AgACAgIAAxkBAAN9aI4I_2A0KeGPH2hplRrrzRh9xS0AApb0MRvoInBI2QgkAtHMAgIBAAMCAANtAAM2BA",
        caption="Soliqdan olingan 2 - hujjat rasmini yuboring"
    )
    await UserGetDatas.PHOTO_TWO.set()


@dp.message_handler(state=UserGetDatas.PHOTO_TWO, content_types=types.ContentType.PHOTO)
async def handle_photo_two(message: types.Message, state: FSMContext):
    await state.update_data(
        photo_two=message.photo[-1].file_id
    )
    await message.answer_photo(
        photo="AgACAgIAAxkBAAN_aI4JKFCo6qQn71YraSHhN7oqt0wAApf0MRvoInBI3OR6872iY_YBAAMCAANtAAM2BA",
        caption="Soliqdan olingan 3 - hujjat rasmini yuboring"
    )
    await UserGetDatas.PHOTO_THREE.set()


@dp.message_handler(state=UserGetDatas.PHOTO_THREE, content_types=types.ContentType.PHOTO)
async def handle_photo_three(message: types.Message, state: FSMContext):
    await state.update_data(
        photo_three=message.photo[-1].file_id
    )
    await message.answer_photo(
        photo="AgACAgIAAxkBAAOBaI4JTGFvsLLYfvuhOh79p-5chf8AApj0MRvoInBI3ilk8WyATWcBAAMCAAN4AAM2BA",
        caption="Panellar soni rasmini yuboring"
    )
    await UserGetDatas.PANELS_COUNT.set()


@dp.message_handler(state=UserGetDatas.PANELS_COUNT, content_types=types.ContentType.PHOTO)
async def handle_panels_count(message: types.Message, state: FSMContext):
    data = await state.get_data()

    if len(data) != 8:
        await message.answer(
            text="Ma'lumotlar to'liq kiritilmadi! Qayta kiriting"
        )
        return

    full_name = data.get("fullname")
    position = data.get("position")
    address = data.get("address")
    invertor_image = data.get("invertor_image")
    panel_model_image = data.get("panel_model_image")
    photo_one = data.get("photo_one")
    photo_two = data.get("photo_two")
    photo_three = data.get("photo_three")

    album = types.MediaGroup()

    album.attach_photo(photo=invertor_image)
    album.attach_photo(photo=panel_model_image)
    album.attach_photo(photo=photo_one)
    album.attach_photo(photo=photo_two)
    album.attach_photo(photo=photo_three,
                       caption=f"Ma'lumotlaringiz qabul qilindi! Tekshirib kerakli tugmani bosing\n\n"
                               f"Ism sharif: {full_name}\n"
                               f"Lavozim: {position}\n"
                               f"Manzil: {address}")
    await message.answer_media_group(media=album)
