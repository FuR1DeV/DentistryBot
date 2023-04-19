from sqlalchemy import desc

from data.models.managers import Manager
from data.models.operators import Operator
from data.models.orders import Orders
from data.models.admin import Admin


async def admin_select(user_id):
    admin = await Admin.query.where(Admin.user_id == user_id).gino.first()
    return admin


async def operator_select(user_id):
    operator = await Operator.query.where(Operator.user_id == user_id).gino.first()
    return operator


async def manager_select(user_id):
    manager = await Manager.query.where(Manager.user_id == user_id).gino.first()
    return manager


async def manager_select_all():
    managers = await Manager.query.gino.all()
    return managers


async def all_orders():
    orders = await Orders.query.gino.all()
    return orders


async def select_order(id_task):
    task = await Orders.query.where(Orders.id == id_task).gino.first()
    return task
