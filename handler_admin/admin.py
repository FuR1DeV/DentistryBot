import csv

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

import states
from bot import bot
from markups import markups
from data.commands import getter, setter


class AdminMain:
    @staticmethod
    async def admin_main(callback: types.CallbackQuery, state: FSMContext):
        await callback.message.edit_text(
            "<b>Добро пожаловать в меню Администратора</b>\n"
            "<b>Вы можете загрузить отчёт Excel или посмотреть статистику</b>",
            reply_markup=markups.Admin.admin_main())
        await state.finish()

    @staticmethod
    async def admin_excel_all_day(callback: types.CallbackQuery):
        all_products = await getter.all_orders()
        with open("all_orders.csv", "w", newline='', encoding="windows-1251") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "Имя Оператора", "Описание Задачи", "Дата создания",
                             "Дата взятия", "Имя Менеджера", "Дата завершения"])
            for i in all_products:
                writer.writerow([i.id, i.operator_name, i.description, i.create_task,
                                 i.get_task, i.manager_name, i.done_task])
        all_orders = InputFile("all_orders.csv")
        await bot.send_document(chat_id=callback.from_user.id,
                                document=all_orders)

