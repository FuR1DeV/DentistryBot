from data.models.managers import Manager
from data.models.operators import Operator
from data.models.orders import Orders


async def operator_add(user_id, username, first_name, last_name):
    """Оператор добавляется в БД"""
    operator = Operator(user_id=user_id, username=username, first_name=first_name,
                        last_name=last_name)
    await operator.create()


async def manager_add(user_id, username, first_name, last_name):
    """Менеджер добавляется в БД"""
    manager = Manager(user_id=user_id, username=username, first_name=first_name,
                      last_name=last_name)
    await manager.create()


async def operator_create_task(user_id, operator_name, description, create_task):
    """Оператор создаёт задачу"""
    task = Orders(operator_user_id=user_id, operator_name=operator_name, description=description, create_task=create_task)
    await task.create()
    return task


async def manager_add_to_task(user_id, first_name, last_name, id_task, get_task):
    """Менеджер добавляется в Задачу"""
    task = await Orders.query.where(Orders.id == id_task).gino.first()
    await task.update(manager_user_id=user_id,
                      manager_name=f"{first_name} {last_name}",
                      get_task=get_task).apply()


async def manager_done_task(id_task, done_task):
    """Менеджер выполняет Задачу"""
    task = await Orders.query.where(Orders.id == id_task).gino.first()
    await task.update(done_task=done_task).apply()
