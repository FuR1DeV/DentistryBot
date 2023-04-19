__all__ = ["register_operator_handler"]

from aiogram import Dispatcher

from .operator import OperatorMain
from states import states


def register_operator_handler(disp: Dispatcher):

    """Operator Main"""

    disp.register_callback_query_handler(OperatorMain.operator_main,
                                         state=["*"],
                                         text="operator_main")
