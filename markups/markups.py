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
                                   callback_data='create_task')
        get1 = InlineKeyboardButton(text='Статистика',
                                    callback_data='operator_statistics')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def create_task():
        approve_ = InlineKeyboardMarkup()
        get = InlineKeyboardButton(text='Создать',
                                   callback_data='operator_create')
        approve_.insert(get)
        return approve_


class Manager:

    @staticmethod
    def manager_main():
        approve_ = InlineKeyboardMarkup()
        get = InlineKeyboardButton(text='Моя задачи',
                                   callback_data='my_tasks')
        get1 = InlineKeyboardButton(text='Статистика',
                                    callback_data='manager_statistics')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def manager_get_task(id_task):
        approve_ = InlineKeyboardMarkup()
        get = InlineKeyboardButton(text='Взять',
                                   callback_data=f'get_task_{id_task}')
        approve_.insert(get)
        return approve_

    @staticmethod
    def manager_done_task(id_task):
        approve_ = InlineKeyboardMarkup()
        get = InlineKeyboardButton(text='Выполнено!',
                                   callback_data=f'done_task_{id_task}')
        approve_.insert(get)
        return approve_
