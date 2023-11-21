from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message()
async def send_answer(message: Message):
    """ Реакция на любое сообщение, что не обрабатывается отдельно. """
    await message.answer(text=LEXICON_RU['other_answer'])
