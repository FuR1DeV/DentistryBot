from sqlalchemy import desc

from data.models.managers import Manager
from data.models.operators import Operator
from data.models.orders import Orders


async def operator_select(user_id):
    operator = await Operator.query.where(Operator.user_id == user_id).gino.first()
    return operator


async def manger_select(user_id):
    manager = await Manager.query.where(Manager.user_id == user_id).gino.first()
    return manager
