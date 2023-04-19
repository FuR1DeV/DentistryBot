__all__ = ["register_admin_handler"]

from aiogram import Dispatcher

from .admin import AdminMain


def register_admin_handler(disp: Dispatcher):

    """Admin Main"""

    disp.register_callback_query_handler(AdminMain.admin_main,
                                         state=["*"],
                                         text="admin_main")
    disp.register_callback_query_handler(AdminMain.admin_excel_all_day,
                                         text_contains="admin_report_all")
