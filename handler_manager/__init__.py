__all__ = ["register_manager_handler"]

from aiogram import Dispatcher

from .manager import ManagerMain
from states import states


def register_manager_handler(disp: Dispatcher):

    """Manager Main"""

    disp.register_callback_query_handler(ManagerMain.manager_main,
                                         state=["*"],
                                         text="manager_main")
    disp.register_callback_query_handler(ManagerMain.get_task,
                                         text_contains="get_task_")
    disp.register_callback_query_handler(ManagerMain.done_task,
                                         text_contains="done_task_")
