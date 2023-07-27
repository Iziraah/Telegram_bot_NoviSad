from aiogram.dispatcher.filters.state import StatesGroup, State


class Form_zakaz(StatesGroup):
    Name = State()
    Surname = State()
    
    
class Form_publik(StatesGroup):
    Name = State()
    Text_ob = State()
    Photo = State()
