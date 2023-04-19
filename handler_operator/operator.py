from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

from bot import bot
from markups import markups
from data.commands import getter, setter
from states import states


class OperatorMain:
    @staticmethod
    async def operator_main(callback: types.CallbackQuery, state: FSMContext):
        operator = await getter.operator_select(callback.from_user.id)
        if not operator:
            await setter.operator_add(callback.from_user.id,
                                      callback.from_user.username,
                                      callback.from_user.first_name,
                                      callback.from_user.last_name)
        await callback.message.edit_text(
            "<b>Добро пожаловать в меню Оператора</b>\n"
            "<b>Вы можете добавить новую задачу или посмотреть статистику</b>",
            reply_markup=markups.Operator.operator_main())
        await state.finish()
