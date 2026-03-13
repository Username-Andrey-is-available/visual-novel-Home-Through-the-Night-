# Home Through the Night — entrypoint and week routing.

label start:
    stop music fadeout 1.0
    call ensure_main_ambience from _call_ensure_main_ambience_6
    show screen deadline_darkness
    show screen gameplay_hud

    scene black
    with fade

    narr "Минск. Конец девяностых."
    narr "После тяжелой смены Паша снова идет домой через дворы."
    narr "Впереди несколько непростых вечеров. И каждый вечер город проверяет его на прочность."

    jump week_loop

label week_loop:
    if day == 1:
        jump day_1
    elif day == 2:
        jump day_2
    elif day == 3:
        jump day_3
    elif day == 4:
        jump day_4
    elif day == 5:
        jump day_5
    elif day == 6:
        jump day_6
    else:
        jump ending_day6_hook
