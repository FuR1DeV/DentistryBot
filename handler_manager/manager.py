from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import bot
from markups import markups
from data.commands import getter, setter


class ManagerMain:

    @staticmethod
    async def manager_main(callback: types.CallbackQuery, state: FSMContext):
        manager = await getter.manager_select(callback.from_user.id)
        if not manager:
            await setter.manager_add(callback.from_user.id,
                                     callback.from_user.username,
                                     callback.from_user.first_name,
                                     callback.from_user.last_name)
        await callback.message.edit_text(
            "<b>Добро пожаловать в меню Менеджера</b>\n"
            "<b>Ждите пока появится новая задача</b>",
            reply_markup=markups.Manager.manager_main())
        await state.finish()

    @staticmethod
    async def get_task(callback: types.CallbackQuery):
        id_task = callback.data.split("_")[2]
        task = await getter.select_order(int(id_task))
        if task.manager_user_id:
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            await bot.send_message(callback.from_user.id,
                                   "Задача уже взята!")
        else:
            await setter.manager_add_to_task(callback.from_user.id,
                                             callback.from_user.first_name,
                                             callback.from_user.last_name,
                                             int(id_task),
                                             datetime.now())
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            await bot.send_message(callback.from_user.id,
                                   "<b>Задача была взята!</b>\n"
                                   "<b>Выполните Задачу:</b>\n\n"
                                   f"<b>{task.description}</b>",
                                   reply_markup=markups.Manager.manager_done_task(task.id))

    @staticmethod
    async def done_task(callback: types.CallbackQuery):
        id_task = callback.data.split("_")[2]
        await setter.manager_done_task(int(id_task), datetime.now())
        await callback.message.edit_text("Данная задача была выполнена!",
                                         reply_markup=markups.Manager.manager_main())
