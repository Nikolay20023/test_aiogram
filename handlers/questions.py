from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from keyboards.inlne_wb import check_button_follow
from aiohttp import ClientSession
from bd.db import get_session
from bd.models import User

router = Router()


async def get_data_from_website(article):
    async with ClientSession() as session:
        url = f"https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}"

        async with session.get(url=url) as response:
            article_data_wb = await response.json()
            return article_data_wb


@router.message(Command("start"))
async def cmd_start(message: Message):
    kb = [
        [KeyboardButton(text="Остановить уведомления"),
         KeyboardButton(text="Получить информацию из бд")],
        [KeyboardButton(text="Получить информацию по товару")],
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите функцию"
    )
    await message.answer(
        "Выберите функцию",
        reply_markup=keyboard,
    )


@router.message(F.text.lower() == "получить информацию по товару")
async def get_data_from_api(message: Message):
    await message.answer(
        "Введите артикуль",
        reply_markup=check_button_follow()
    )


@router.message(F.text.lower() == "получить информацию из бд")
async def get_bd(message: Message):
    await message.answer(
        message.text,
        reply_markup=check_button_follow()
    )


@router.message(F.text.lower() == "остановить уведомления")
async def stop_notification(message: Message):
    await message.answer(
        message.text,
        reply_markup=check_button_follow()
    )


@router.message(F.text.lower())
async def get_data(message: Message):
    data = await get_data_from_website(message.text)
    # await message.answer(
    #     data.data,
    #     reply_markup=check_button_follow()
    # )
    sum_ = [x for x in data['data']['products'][0]['promotions']]
    await message.answer(
        f"Название: {data['data']['products'][0]['name']}\n"
        f"Артикул: {data['data']['products'][0]['id']}\n"
        f"Цена: {data['data']['products'][0]['salePriceU']}\n"
        f"Рейтинг: {data['data']['products'][0]['reviewRating']}\n"
        f"Количество: {sum(sum_)}",
        reply_markup=check_button_follow()
    )

    async with get_session() as session:
        user = User(
            id=message.from_user.id,
            name=data['data']['products'][0]['name']
        )
        session.add(user)

        await session.commit
