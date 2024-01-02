from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from assets.group import group
from keyboards import main_keyboard, settings_keyboard
from callback.functions import Functions
from assets.config import URL
import json

router = Router()
cmd = Functions()


@router.message(CommandStart())
async def start_cmd(msg: Message):
    if cmd.user_exists(msg.from_user.id):
        await msg.answer(f"Привет, {msg.from_user.first_name}! Ты уже зарегистрирован у меня. "
                         f"Повторно вводить команду не нужно!")
    else:
        welcome_message = (f"Привет, {msg.from_user.first_name}! Я Джек, помощник в отслеживании изменений в "
                           f"расписании.\nЕсли ты хочешь, чтобы я отправлял тебе расписание твоей группы,то укажи, "
                           f"пожалуйста, для начала её название.\n<i>Пример: МК-22</i>")
        sticker_hi = 'CAACAgIAAxkBAAEFxFRjFnKx2k7rTEcWbXsJu0z5xlTMUwACiBEAArOMcUnCJQLlwkLsoikE'

        await msg.answer_sticker(sticker_hi)
        await msg.answer(welcome_message)
        cmd.add_user(msg)


@router.message()
async def user_cmd(msg: Message):
    if cmd.group_exists(msg.from_user.id):
        if msg.text.lower() == "расписание 📅":
            pass
        elif msg.text.lower() == "звонки 🔔":
            await msg.answer(cmd.answer_bell())
        elif msg.text.lower() == "помощь 📞":
            await msg.answer("В случае возникновения каких либо вопросов/ошибок обращайтесь к @skr1pmen. "
                             "В начале сообщения указал #JackBot")
        else:
            await msg.answer("Прости, но я тебя не понимаю 😞")
    else:
        for name, code in group.items():
            if name == msg.text.lower():
                cmd.edit_group(msg.from_user.id, code)
                await msg.answer(
                    "Хорошо, теперь ты будешь получать расписание этой группы.",
                    reply_markup=main_keyboard.main(f"{URL}{cmd.get_code(msg.from_user.id)}"))
                break
        else:
            await msg.answer("Прости, но я не знаю такую группу😥\nПопробуй ещё раз или обратись в поддержку!")
