from data.models.managers import Manager
from data.models.operators import Operator
from data.models.orders import Orders


async def operator_add(user_id, username, first_name, last_name):
    """Оператор добавляется в БД"""
    operator = Operator(user_id=user_id, username=username, first_name=first_name,
                        last_name=last_name)
    await operator.create()
