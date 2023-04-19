from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


def start():
    approve_ = InlineKeyboardMarkup()
    get = InlineKeyboardButton(text='Оператор',
                               callback_data='operator_main')
    get1 = InlineKeyboardButton(text='Менеджер',
                                callback_data='manager_main')
    approve_.insert(get)
    approve_.insert(get1)
    return approve_


class Operator:

    @staticmethod
    def operator_main():
        approve_ = InlineKeyboardMarkup()
        get = InlineKeyboardButton(text='Создать Задачу',
                                   callback_data='operator_create_task')
        get1 = InlineKeyboardButton(text='Статистика',
                                    callback_data='operator_statistics')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_
