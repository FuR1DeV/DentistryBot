from aiogram import types, executor
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from data.commands import getter, setter
from handler_operator import register_operator_handler
from handler_manager import register_manager_handler
from handler_admin import register_admin_handler
from settings import config
from markups import markups


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Выберите вашу роль",
                           reply_markup=markups.start())


@dp.message_handler(Command("admin"), state=["*"])
async def admin(message: types.Message, state: FSMContext):
    await state.finish()
    if str(message.from_user.id) in config.ADMIN_ID:
        admin_ = await getter.admin_select(message.from_user.id)
        if not admin_:
            await setter.admin_add(message.from_user.id,
                                   message.from_user.username,
                                   message.from_user.first_name,
                                   message.from_user.last_name)
        await bot.send_message(message.from_user.id,
                               "<b>Добро пожаловать в меню Администратора</b>\n"
                               "<b>Вы можете загрузить отчёт Excel или посмотреть статистику</b>",
                               reply_markup=markups.Admin.admin_main())
    else:
        await bot.send_message(message.from_user.id, "У вас нет прав доступа!")


async def on_startup(_):
    # asyncio.create_task(scheduler())

    from data import db_gino
    print("Database connected")
    await db_gino.on_startup(dp)

    """Удалить БД"""
    # await db.gino.drop_all()

    """Создание БД"""
    await db_gino.db.gino.create_all()

    """Регистрация хэндлеров"""
    register_operator_handler(dp)
    register_manager_handler(dp)
    register_admin_handler(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
