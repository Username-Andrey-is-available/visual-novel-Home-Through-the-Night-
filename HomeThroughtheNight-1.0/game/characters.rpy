# Characters

# Главный герой и базовые

init python:
    def npc_time_callback(event, interact=True, **kwargs):
        if event == "end" and getattr(store, "clock_running", False):
            store.game_minutes += 1

define p = Character('Паша', color="#d6d6ff")
define narr = Character(None)

# Положительные
define guy = Character('Игорь', color="#b7e1ff", callback=npc_time_callback)
define lesha = Character('Лёша', color="#d8f2ff", callback=npc_time_callback)
define dvornik = Character('Дворник Семёныч', color="#d6ffd6", callback=npc_time_callback)
define student = Character('Студентка Лина', color="#8a2be2", callback=npc_time_callback)
define librarian = Character('Библиотекарь Марат', color="#00ffff", callback=npc_time_callback)

# Плохие
define gop = Character('Санек', color="#d3d3d3", callback=npc_time_callback)
define cop = Character('Климов', color="#d3d3d3", callback=npc_time_callback)
define broker = Character('Рома Темщик', color="#d3d3d3", callback=npc_time_callback)
define debt = Character('Коллектор Гена', color="#d3d3d3", callback=npc_time_callback)
define thief = Character('Карманник Лёня', color="#d3d3d3", callback=npc_time_callback)
define faceless = Character('Паша', color="#d6d6ff")


# Аномальные
define neck = Character('Женщина с длинной шеей', color="#ff0000", callback=npc_time_callback)
define smile = Character('Улыбающийся мужчина', color="#ff7f00", callback=npc_time_callback)
define thin = Character('Очень высокий худой', color="#ffff00", callback=npc_time_callback)
define teeth = Character('Человек с частыми зубами', color="#00ffff", callback=npc_time_callback)
define blink = Character('Редко моргающий', color="#0000ff", callback=npc_time_callback)
define oldw = Character('Тамара Петровна', color="#adff2f", callback=npc_time_callback)

