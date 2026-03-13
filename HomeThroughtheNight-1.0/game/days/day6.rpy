# Day 6 (secret)

label day_6:
    call ensure_main_ambience from _call_ensure_main_ambience_5
    call stop_day_clock from _call_stop_day_clock_6

    scene black
    with dissolve
    narr "Суббота. Ты просыпаешься до рассвета и впервые не чувствуешь, что идешь по чужому маршруту."
    p "Сегодня без часов. Мне надоело жить по стрелкам, будто кто-то снаружи мерит мою вину минутами."
    p "Я попробую прожить день целиком и не провалиться между кадрами."

    if day3_student_date_agreed:
        call day6_lina_route from _call_day6_lina_route
    else:
        narr "Лины рядом нет. Ты идешь один, проверяя шаги, как будто заново учишься ходить."

    call day6_home_sewing from _call_day6_home_sewing
    call day6_final_resolution from _call_day6_final_resolution
    return


label day6_lina_route:
    scene expression bg_path("/streets/street_id_2")
    with dissolve
    call show_right(["student", "girl", "lina"], ["default", "idle"]) from _call_show_right_45
    student "Ты пришел. Я уже думала, ты снова исчезнешь без объяснений."
    p "Не исчезну. Давай просто пройдемся вместе."
    $ day6_lina_met = True

    scene expression bg_path("/garages/garage_id_2")
    with dissolve
    narr "Вы проходите мимо гаражей, где раньше всегда кто-то шумел."
    student "Тут как будто тише, чем должно быть."

    scene expression bg_path("/buildings/kiosk")
    with dissolve
    narr "У киоска пусто. Витрина отражает вас двоих как двух разных людей из разных жизней."

    scene expression bg_path("/buildings/pharmacy")
    with dissolve
    narr "Возле аптеки Лина берет тебя за рукав, будто проверяет, что ты настоящий."

    scene expression bg_path("/courtyards/yard_id_3")
    with dissolve
    narr "Во дворе под аркой вы молчите дольше обычного."

    scene expression bg_path("/buildings/factory_exit_id_2")
    with dissolve
    narr "Последней точкой становится завод. Вы медленно проходите мимо проходной."

    if toughness < 9:
        scene black
        with fade
        p "Темно."
        p "Снова провал. Никаких часов, никаких отметок — только разрыв между двумя шагами."
        p "Почему я снова не помню путь между двумя шагами?"

        scene expression bg_path("/abandoned/abandoned_id_1")
        with dissolve
        call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_11
        narr "Ты приходишь в себя на заброшке. Воздух пахнет сырой ржавчиной."
        call show_right("Lina_idle") from _call_show_right_46
        narr "В свете фонаря — мертвое тело Лины."
        p "Нет. Нет! Нет!!! Почему..."
        $ lina_die = True
        $ day6_lina_alive = False

        if empathy < toughness:
            jump ending_day6_hook

        call stress_up(2) from _call_stress_up_33
        call hide_right from _call_hide_right_45
        call restore_main_ambience from _call_restore_main_ambience_13
    else:
        scene expression bg_path("/streets/street_id_2")
        with dissolve
        narr "Ты с усилием отводишь взгляд от проходной и продолжаешь идти рядом с Линой."
        student "Ты дрожишь."
        p "Уже лучше. Главное — не останавливаться."
        narr "Ты провожаешь Лину до остановки. Перед отъездом она коротко обнимает тебя."
        student "До скорого, Паша."
        $ day6_lina_alive = True
        $ empathy += 3

    call hide_right from _call_hide_right_46
    return


label day6_home_sewing:
    scene expression bg_path("/entrances/my_room")
    with dissolve
    narr "Вернувшись домой, ты берешь старую игрушку без лица."

    menu:
        "Взять иголки и аккуратно зашить лицо игрушке.":
            $ day6_used_needles = True
            p "Хватит пустых масок. Пусть у этого лица будут швы, но оно будет настоящим."

        "Взять спицы и зашить лицо грубыми стежками.":
            $ day6_used_spokes = True
            p "Если чинить, то до конца. Даже если выйдет грубо."
            narr "Из пустой комнаты слышится голос, будто из памяти:"
            narr "«Я-то тебя давно уж простила, подумай о других.»"

    return


label day6_final_resolution:
    if day5_oldwoman_hint and empathy > 8:
        scene black
        with fade
        narr "Вспоминая слова Тамары Петровны, ты добровольно ложишься на лечение в клинику."

        if stress < 7:
            menu:
                "Избавиться от улик дома перед госпитализацией.":
                    $ day6_disposed_evidence = True
                    $ day5_disposed_gun = True
                    narr "Ночью ты избавляешься от свертка с уликами и сжигаешь окровавленные тряпки."
                "Ничего не трогать и ехать в клинику сразу, ведь непонятно кода Он вернётся.":
                    $ day6_disposed_evidence = False
                    narr "Ты оставляешь квартиру как есть и уезжаешь в клинику."
        else:
            narr "Стресс не дает собраться, ты так и не решаешься вернуться к тайнику с уликами."
            $ day6_disposed_evidence = False

        if not day6_disposed_evidence:
            scene black
            with fade
            narr "Проходит месяц лечения."
            narr "У ворот клиники тебя встречают Климов и двое в штатском."
            narr "Тебя забирают в тюрьму: улики нашли там, где ты их оставил."
            jump ending_prison
        else:
            scene black
            with fade
            narr "Курс длится несколько месяцев. Ночи становятся тише."
            narr "В темноте слышится спокойный голос Марата:"
            narr "Марат: 'Запомни, мой друг, смерть — это только начало.'"

        if day6_used_needles and day6_lina_alive:
            jump ending_good_lina_doll
        else:
            jump ending_clinic

    if day6_used_needles and day6_lina_alive:
        jump ending_good_lina_doll

    scene black
    with fade
    narr "Суббота заканчивается без ответов. Но впервые ты дошел до конца дня и всё помнишь."
    narr "'Мы не можем выбирать внешние обстоятельства, но всегда можем выбрать отношение к ним.' — Эпиктет."
    narr "'Кто долго смотрит в бездну, в того бездна тоже вглядывается.' — Ницше."
    p "Успел ли я зашить бездну?"
    narr "Плохая концовка: хрупкое равновесие."
    $ renpy.full_restart()


label ending_good_lina_doll:
    call stop_day_clock from _call_stop_day_clock_7
    hide screen deadline_darkness
    hide screen gameplay_hud
    scene expression bg_path("/endings/lina_doll")
    with fade
    narr "Проходит десять лет."
    narr "Ты и Лина живете вместе: тихо, бережно."
    narr "Второе 'я' осталось в старой кукле с зашитым лицом и больше не выходит наружу."
    narr "Нераскрытая череда убийств десятилетней давности до сих пор ночями пробуждает страх в сердцах горожан."
    if $empathy > 9:
        narr "Хорошая концовка: стойкость и везение."
    else:
        narr "А в вашем сердце незашиваемая дыра."
        narr "концовка: Пирова победа."
    $ renpy.full_restart()
