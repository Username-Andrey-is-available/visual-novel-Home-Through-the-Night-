# Characters

# Главный герой и базовые

init python:
    def npc_time_callback(event, interact=True, **kwargs):
        if event == "end" and getattr(store, "clock_running", False):
            store.game_minutes += 1

define p = Character(_('Паша'), color="#d6d6ff")
define narr = Character(None)

# Положительные
define guy = Character(_('Игорь'), color="#b7e1ff", callback=npc_time_callback)
define lesha = Character(_('Лёша'), color="#d8f2ff", callback=npc_time_callback)
define dvornik = Character(_('Дворник Семёныч'), color="#d6ffd6", callback=npc_time_callback)
define student = Character(_('Студентка Лина'), color="#8a2be2", callback=npc_time_callback)
define librarian = Character(_('Библиотекарь Марат'), color="#00ffff", callback=npc_time_callback)

# Плохие
define gop = Character(_('Санек'), color="#d3d3d3", callback=npc_time_callback)
define cop = Character(_('Климов'), color="#d3d3d3", callback=npc_time_callback)
define broker = Character(_('Рома Темщик'), color="#d3d3d3", callback=npc_time_callback)
define debt = Character(_('Коллектор Гена'), color="#d3d3d3", callback=npc_time_callback)
define thief = Character(_('Карманник Лёня'), color="#d3d3d3", callback=npc_time_callback)
define faceless = Character(_('Паша'), color="#d6d6ff")


# Аномальные
define neck = Character(_('Женщина с длинной шеей'), color="#ff0000", callback=npc_time_callback)
define smile = Character(_('Улыбающийся мужчина'), color="#ff7f00", callback=npc_time_callback)
define thin = Character(_('Очень высокий худой'), color="#ffff00", callback=npc_time_callback)
define teeth = Character(_('Человек с частыми зубами'), color="#00ffff", callback=npc_time_callback)
define blink = Character(_('Редко моргающий'), color="#0000ff", callback=npc_time_callback)
define oldw = Character(_('Тамара Петровна'), color="#adff2f", callback=npc_time_callback)

