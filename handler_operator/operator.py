from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

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

    @staticmethod
    async def create_task(callback: types.CallbackQuery):
        await callback.message.edit_text("Опишите задачу",
                                         reply_markup=markups.Operator.create_task())
        await states.OperatorStates.description.set()

    @staticmethod
    async def description(message: types.Message, state: FSMContext):
        result = message.text
        task = await setter.operator_create_task(message.from_user.id,
                                                 f"{message.from_user.first_name} "
                                                 f"{message.from_user.last_name}",
                                                 result,
                                                 datetime.now())
        managers = await getter.manager_select_all()
        await bot.send_message(message.from_user.id,
                               "Задача была создана!",
                               reply_markup=markups.Operator.operator_main())
        for i in managers:
            await bot.send_message(i.user_id,
                                   f"ID задачи - <b>{task.id}</b>\n\n"
                                   f"Оператор - <b>{task.operator_name}</b>\n\n"
                                   f"Описание:\n<b>{task.description}</b>\n\n"
                                   f"Создано - <b>{datetime.strftime(task.create_task, '%d-%m-%Y, %H:%M:%S')}</b>",
                                   reply_markup=markups.Manager.manager_get_task(task.id))
        await state.finish()
