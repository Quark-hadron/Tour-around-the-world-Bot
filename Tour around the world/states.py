from aiogram.fsm.state import State, StatesGroup

class TourSelection(StatesGroup):
    selecting_people = State()
    selecting_season = State()
    selecting_tour_type = State()
    neuro_search = State() 