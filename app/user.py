from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.generate import ai_generate

user = Router()


class Gen(StatesGroup):
    wait = State()


@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! 🤖 Я твой ИИ-помощник. Готов ответить на любой вопрос. Чем могу помочь?"
    )


@user.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer("Подождите, ваш запрос генерируется.")


@user.message()
async def generating(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text)
    await message.answer(response)
    await state.clear()
