# Endings

label ending_burnout:
    call stop_day_clock from _call_stop_day_clock_8
    hide screen deadline_darkness
    hide screen gameplay_hud
    scene black
    with fade
    narr "Ты доходишь до подъезда, но стоишь перед дверью, словно впервые в этом районе."
    narr "Неделя еще не кончилась, а силы уже закончились."
    narr "Кто-то за вас открыл дверь, вы теперь пассажир в теле."
    narr "Плохая концовка: стресс."

    $ renpy.full_restart()

label ending_lost_night:
    call stop_day_clock from _call_stop_day_clock_9
    hide screen deadline_darkness
    hide screen gameplay_hud
    scene black
    with fade
    narr "Утром дворник находит тебя в сугробе у пустой остановки."
    narr "Ты без сознания, губы синие от холода, а в зубах зажата бумажная полоска."
    narr "На записке дрожащий почерк: \"Тьма поглотила мою душу раньше, чем тело. Я свободен от себя.\""
    narr "Плохая концовка: ночь пережила именно тебя."
    $ renpy.full_restart()

label ending_prison:
    call stop_day_clock from _call_stop_day_clock_10
    hide screen deadline_darkness
    hide screen gameplay_hud
    scene expression bg_path("/endings/prison")
    with fade
    narr "Сирена режет ночь, а холодный асфальт пахнет железом и пылью."
    narr "Климов молча защелкивает наручники: разговоров уже не будет."
    narr "Плохая концовка: ты перешел черту и закончил за решеткой."
    $ renpy.full_restart()

label ending_faceless_function:
    call stop_day_clock from _call_stop_day_clock_11
    hide screen deadline_darkness
    hide screen gameplay_hud
    scene expression bg_path("/endings/faceless")
    with fade
    narr "Ты смотришь в зеркало и не узнаешь выражение собственного лица."
    narr "Черты будто стираются, уступая место удобной маске для любой смены и любого маршрута."
    narr "Плохая концовка: ты так и не раскрыл собственную тайну."
    $ renpy.full_restart()

label ending_suicide:
    call stop_day_clock from _call_stop_day_clock_12
    hide screen deadline_darkness
    hide screen gameplay_hud
    scene expression bg_path("/endings/suicide")
    with fade
    narr "Ты понимаешь, что внутри тебя слишком много голосов, и один из них делает город темнее."
    narr "От ужаса и вины ты выбираешь тишину как единственный выход."
    narr "Трагическая концовка: Паша не выдержал правды о себе."
    $ renpy.full_restart()

label ending_blood_tools:
    call stop_day_clock from _call_stop_day_clock_13
    hide screen deadline_darkness
    hide screen gameplay_hud
    scene black
    with fade
    narr "Ты обыскиваешь квартиру и находишь сверток с кровавыми орудиями."
    $ toughness -= 1
    if toughness <= 4:
        p "'Это другого меня... но враг ли я ему?' — думаешь ты, не находя в себе сил бороться."
    else:
        p "'Фабрика, дом, сон, фабрика... Нет, не так. В пекло!'"
    $ day = 6
    jump week_loop

label ending_clinic:
    call stop_day_clock from _call_stop_day_clock_14
    hide screen deadline_darkness
    hide screen gameplay_hud
    scene expression bg_path("/endings/clinic")
    with fade
    narr "Осознавая страшную правду, ты ложишься в платную клинику."
    narr "Проходит три года."
    if toughness >= 7:
        narr "Ты выписываешься и чувствуешь себя как никогда спокойно: аномальные больше не приходят по ночам."
    else:
        narr "Врачи считают лечение успешным."
        narr "Возможно, другой спит пока не встретит фиолетовый."
    narr "Особая (лучшая) концовка: попытка лечения."
    $ renpy.full_restart()

label ending_day6_hook:
    call stop_day_clock from _call_stop_day_clock_15
    hide screen deadline_darkness
    hide screen gameplay_hud
    scene black
    with fade
    p "Я больной человек."
    p "Я слепец, который даёт свободу другому Я и крепко-накрепко закрытыми глазами."
    p "Все эти 'люди'... они когда-то были людьми, пока..."
    p "пока я не убил их."
    p "Но я хочу жить. Виноват ли я в сосуществовании с монстром, что живёт во мне?!"
    faceless "Радуга собрана."
    p "Надо ложиться спать, завтра воскресенье, не помню, что я делаю в воскресенье,"
    p "а послезавтра понедельник, люблю понедельник, я вернусь домой и буду ждать следующий день."
    narr "Истинная концовка: всё осознал и смирился с кошмаром."
    $ renpy.full_restart()
