from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from db.db_work import create_table

router: Router = Router()


@router.message(CommandStart())
async def main_menu(message: Message):
    await message.answer(text='Hello!')
    await create_table()
