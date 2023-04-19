from aiogram.dispatcher.filters.state import State, StatesGroup


class OperatorStates(StatesGroup):
    description: State = State()


class ManagerStates(StatesGroup):
    done: State = State()
