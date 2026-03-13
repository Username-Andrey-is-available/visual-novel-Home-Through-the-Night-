# Day 3

label day_3:
    call ensure_main_ambience from _call_ensure_main_ambience_2
    call init_day_clock(0, 0) from _call_init_day_clock_2

    scene black
    with dissolve
    narr "00:00. До выхода из фабрики еще целый день — пока только сон и тяжелые мысли."
    narr "Среда. Перед выходом Паша снова проваливается в сон, будто спускается в сырой колодец памяти."

    if day2_lost_roma_package:
        narr "Во сне он бежит по двору, но снег превращается в стекло, и каждый шаг режет подошвы."
        narr "Сзади звучит голос Ромы: спокойный, почти добрый, от этого еще страшнее."
        p "Я просыпаюсь раньше будильника, как после удара током. Пальцы дрожат, в горле сухо."
        call stress_up(1) from _call_stress_up_8
    else:
        p "Странно, но сегодня мысли не скатываются сразу в мрак."
        p "Вчера ночью вспоминал Пруста: память часто сильнее воли, а запахи и мелочи вытаскивают целые годы."
        p "И еще Камю: даже в абсурде есть выбор — не быть подлецом, когда никто не видит."
        if day2_easy_money_done:
            narr "После истории с пакетом Ромы Паша впервые за долгое время просыпается с ясной головой."
            p "Не то чтобы счастливый... но будто внутри впервые не скрипит ржавчина."
            $ stress = max(0, stress - 1)

    scene expression bg_path("start-game_id_3")
    with dissolve
    call init_day_clock(20, 30) from _call_init_day_clock_3
    narr "20:30. Смена закончилась, Паша выходит с фабрики в холодный вечер."
    call apply_shift_bonus from _call_apply_shift_bonus_1
    narr "Вечер холодный и прозрачный, будто город специально выставил все контуры резче."
    p "Странно, что саму смену я помню кусками: цех, сирена, и сразу проходная."

    call day3_random_old_faces from _call_day3_random_old_faces
    call day3_bad_thief_scene from _call_day3_bad_thief_scene
    call day3_dvornik_scene from _call_day3_dvornik_scene
    call day3_librarian_scene from _call_day3_librarian_scene
    call day3_student_scene from _call_day3_student_scene
    call day3_lost_package_debt_branch from _call_day3_lost_package_debt_branch

    scene expression bg_path("/entrances/entrance_id_1")
    with dissolve
    narr "Паша стоит у двери подъезда и слушает, как в батареях щелкает горячая вода."
    p "Третий день пережил. Значит, можно пережить и четвертый."

    call stop_day_clock from _call_stop_day_clock_2
    $ day += 1
    jump week_loop


label day3_random_old_faces:
    $ old_faces = renpy.random.sample(["sanek", "oldw", "igor", "lesha"], 2)

    $ current_face = old_faces[0]
    call day3_old_face_once from _call_day3_old_face_once
    $ current_face = old_faces[1]
    call day3_old_face_once from _call_day3_old_face_once_1

    return


label day3_old_face_once:
    if current_face == "sanek":
            narr "У поворота к гаражам Паша замечает знакомый силуэт в спортивной куртке."
            scene expression bg_path("/garages/garage_id_2")
            with dissolve
            call show_right(["gopnik", "sanek"], ["default", "idle"]) from _call_show_right_11
            gop "Пашка. Сегодня без поборов, расслабься."
            gop "Но район на взводе: чужих лиц стало много."
            menu:
                "Поддержать разговор и не провоцировать конфликт.":
                    p "Понял. Спасибо, что предупредил."
                    gop "Не благодари, просто смотри по сторонам."
                    $ empathy += 1

                "Отмахнуться с раздражением.":
                    p "Да все вы одинаковые: сначала пугаете, потом советы раздаете."
                    gop "Дело твое. Потом не говори, что не предупреждали."
                    call stress_up(1) from _call_stress_up_9
            call hide_right from _call_hide_right_14

    elif current_face == "oldw":
            narr "На лавки под фонарем сидит Тамара Петровна и вяжет в полутьме."
            scene expression bg_path("/courtyards/yard_id_3")
            with dissolve
            call show_right(["oldw", "oldwoman", "babka"], ["default", "idle"]) from _call_show_right_12
            oldw "Сынок, у тебя взгляд сегодня усталый."
            menu:
                "Остановиться и спокойно ответить.":
                    p "Есть такое. Но, кажется, я держусь."
                    oldw "Держись не зубами, а сердцем. Так дольше выйдет."
                    $ empathy += 1

                "Сделать вид, что не услышал.":
                    narr "Ты проходишь мимо, чувствуя на спине ее долгий взгляд."
                    call stress_up(1) from _call_stress_up_10
            call hide_right from _call_hide_right_15

    elif current_face == "igor":
            narr "На углу у остановки Игорь нервно курит и оглядывается на арку."
            scene expression bg_path("/streets/street_id_2")
            with dissolve
            call show_right(["boy", "guy", "igor"], ["default", "idle"]) from _call_show_right_13
            guy "Паш, помнишь того без лица? Вчера снова видел силуэт у арки."
            menu:
                "Поговорить серьезно.":
                    p "Если увидишь снова — иди в людное место и звони знакомым. Не стой один."
                    guy "Ты прав. Просто страшно, что мне уже верить себе трудно."
                    $ toughness += 1

                "Пошутить не к месту.":
                    p "Может, это твой будущий начальник."
                    guy "Очень смешно..."
                    call stress_up(1) from _call_stress_up_11
            call hide_right from _call_hide_right_16

    elif current_face == "lesha":
            narr "У подъезда Пашу окликает Лёша, поправляя рукав рабочей куртки."
            scene expression bg_path("/entrances/entrance_id_2")
            with dissolve
            call show_right(["lesha", "guy"], ["default", "idle"]) from _call_show_right_14
            lesha "О, сосед по маршруту. Как сам?"
            menu:
                "Спросить про его ребенка.":
                    p "Сын дома нормально?"
                    lesha "Нормально. Спасибо, что тогда не прошел мимо."
                    $ empathy += 1

                "Быстро свернуть разговор.":
                    p "Слушай, без обид, сил говорить нет."
                    lesha "Понимаю. Бывает."
            call hide_right from _call_hide_right_17

    return


label day3_bad_thief_scene:
    scene expression bg_path("/buildings/magazine_id_1")
    with dissolve
    call show_right(["thief", "lenya"], ["default", "idle"]) from _call_show_right_15

    narr "У ларька к тебе прилипает худой парень в дешевом костюме."
    thief "Брат, выручай на проезд. Сам видишь — беда."
    narr "Пока он говорит, его пальцы слишком внимательно смотрят на твой карман."

    menu:
        "Дать 5 рублей и уйти без конфликта.":
            if money >= 5:
                $ money -= 5
                p "Держи и не лезь к людям в карманы."
                thief "Да понял я, понял..."
                $ empathy += 1
            else:
                p "Нечего давать."
                thief "Тогда и просить нечего."

        "Поймать его за руку и прижать к стене.":
            p "Карман щупать вздумал?"
            thief "Ладно, отпусти, ошибся!"
            menu:
                "Отпустить после предупреждения.":
                    p "Исчезни, пока цел."
                    thief "Уже ушел..."

                "Потребовать компенсацию 10 рублей.":
                    if toughness >= 2:
                        p "Десятку за урок. Быстро."
                        thief "Ты хуже ментов..."
                        $ money += 10
                        $ toughness += 1
                    else:
                        p "Слышь... давай десятку за урок..."
                        thief "ЧЕГО?! Иди отсюда."
                        $ toughness -= 1

        "Оттолкнуть его и ускориться.":
            narr "Ты дергаешься слишком резко, и парень успевает вытащить из кармана смятую купюру."
            if money > 0:
                $ stolen = min(money, 15)
                $ money -= stolen
                narr "Пропало [stolen] ₽."
            call stress_up(1) from _call_stress_up_12

    call hide_right from _call_hide_right_18
    return


label day3_dvornik_scene:
    scene expression bg_path("/courtyards/yard_id_3")
    with dissolve
    call show_right(["dvornik", "oldman"], ["default", "idle"]) from _call_show_right_16

    dvornik "Паша, стой. Ты же с завода идешь каждый вечер, верно?"
    p "Верно, Семёныч."
    dvornik "Я людей по шагу узнаю. У тебя шаг стал тяжелее."
    narr "Семёныч опирается на метлу, как на посох, и вдруг говорит почти шепотом."
    dvornik "В четверг поговори с Человеком Без Лица. Что бы это ни значило — выслушай его до конца."
    p "Семёныч... это шутка такая?"
    dvornik "Хотел бы, чтобы шутка. Только не спорь, ладно?"

    $ day3_met_dvornik = True
    $ day3_face_man_hint = True

    menu:
        "Отнестись серьезно и поблагодарить.":
            p "Хорошо. Спасибо за предупреждение."
            dvornik "Вот и молодец. Иногда правильно молчать и слушать."
            $ empathy += 1

        "Скептически усмехнуться.":
            p "Семёныч, тебе бы романы писать."
            dvornik "Смейся, пока можешь. Ночь любит самоуверенных."
            call stress_up(1) from _call_stress_up_13

    if not day3_dvornik_refused_rematch:
        call day3_dvornik_rps_loop from _call_day3_dvornik_rps_loop

    call hide_right from _call_hide_right_19
    return


label day3_dvornik_rps_loop:
    while money >= 3 and day3_dvornik_money > 0 and not day3_dvornik_refused_rematch:
        menu:
            "Предложить Семёнычу сыграть в камень-ножницы-бумага на 3 рубля.":
                p "Семёныч, давай в камень-ножницы-бумага? По 3 рубля раунд."
                dvornik "Эх, молодежь... Ладно, давай."
                menu:
                    "Камень.":
                        $ p_rps = "камень"
                    "Ножницы.":
                        $ p_rps = "ножницы"
                    "Бумага.":
                        $ p_rps = "бумага"

                $ d_rps = renpy.random.choice(["камень", "ножницы", "бумага"])
                dvornik "У меня [d_rps]."

                if p_rps == d_rps:
                    narr "Ничья. Деньги остаются при вас."
                    $ day3_dvornik_win_streak = 0
                elif (p_rps == "камень" and d_rps == "ножницы") or (p_rps == "ножницы" and d_rps == "бумага") or (p_rps == "бумага" and d_rps == "камень"):
                    $ money += 3
                    $ day3_dvornik_money = max(0, day3_dvornik_money - 3)
                    $ day3_dvornik_win_streak = 0
                    p "Мой раунд."
                    dvornik "Забирай свои три рубля."
                else:
                    $ money -= 3
                    $ day3_dvornik_money += 3
                    $ day3_dvornik_win_streak += 1
                    dvornik "Старость помнит комбинации лучше молодости."

                if day3_dvornik_money <= 0:
                    dvornik "Всё, Паша. Денег не осталось. На сегодня игры закончены."
                    return

                if day3_dvornik_win_streak >= 3:
                    dvornik "Будет тебе уроком."
                    narr "Семёныч убирает деньги в карман, разворачивается и уходит, не давая отыграться."
                    $ day3_dvornik_refused_rematch = True
                    return

            "Не играть и идти дальше.":
                return

    if money < 3:
        p "Без трех рублей даже предлагать неудобно."
    elif day3_dvornik_money <= 0:
        dvornik "Паша, у меня пусто. В другой раз сыграем."

    return


label day3_librarian_scene:
    scene expression bg_path("/buildings/kiosk")
    with dissolve
    call play_safe_dialog_music("libr-theme.mp3") from _call_play_safe_dialog_music
    call show_right(["librarian", "man"], ["default", "idle"]) from _call_show_right_17

    narr "У газетного киоска мужчина и поправляет стопку потрепанных книг."
    librarian "Молодой человек, не хотите обмен: книга на книгу или книга на разговор?"
    p "На разговор у меня денег точно хватит."
    librarian "Тогда вопрос: что важнее — правда, которая ранит, или ложь, которая лечит?"
    librarian "Меня тревожит, что люди разучились задавать вопросы, на которые не хотят слышать ответ."
    librarian "Я читаю стоиков по ночам, но утром все равно просыпаюсь с ощущением надвигающейся беды."

    menu:
        "Дополнить цитату: 'Не вещи тревожат людей, а...'.":
            p "...мнения о вещах. Эпиктет."
            librarian "Редкий собеседник."
            librarian "Ты каждый вечер выходишь с фабрики чтобы прийти домой, когда ты последний раз выходил из дома чтобы прийти на фабрику?"
            p "Я... не знаю, что ответить."
            $ day3_librarian_factory_phrase_heard = True
            $ empathy += 1

        "Отшутиться и перевести тему на погоду.":
            p "Тревожит всех, особенно когда снег с дождем."
            librarian "Погода — хороший способ не говорить о главном."
            $ stress += 1

    librarian "Всё-же ответь на вопрос."

    menu:
        "Правда, если после нее можно действовать.":
            p "Ложь лечит только до первого столкновения с реальностью."
            librarian "Неплохой ответ. Держите." 
            narr "Марат протягивает тонкую брошюру без обложки: внутри цитаты о страхе и свободе."
            if "брошюра Марата" not in inventory:
                call add_item("брошюра Марата") from _call_add_item_2
            $ empathy += 1

        "Ложь, если человеку и так плохо.":
            p "Иногда человеку нужно сначала выжить, а потом уже слушать правду."
            librarian "Практик, значит. Это тоже честно."
            $ toughness += 1

        "Сказать, что философия — роскошь для сытых.":
            p "Когда в кошельке пусто, спорить о правде странно."
            librarian "Тогда возьмите прагматичный совет: даже 3 рубля в день откладывать лучше, чем ждать чуда."
            menu:
                "Послушать совет и отложить 3 рубля.":
                    if money >= 3:
                        $ money -= 3
                        narr "Ты убираешь 3 ₽ в отдельный карман 'на черный день'."
                        $ stress = max(0, stress - 1)
                    else:
                        p "Откладывать нечего."
                "Отмахнуться и уйти.":
                    call stress_up(1) from _call_stress_up_14

    menu:
        "Купить в киоске тест на стресс (10 ₽).":
            if money >= 10:
                $ money -= 10
                if stress <= 2:
                    narr "Тест показывает: внутри пока тихо, но это хрупкое равновесие."
                elif stress <= 4:
                    narr "Тест показывает: напряжение уже накопилось и мешает дышать свободно."
                else:
                    narr "Тест показывает: ты держишься на нервах, организм работает на износ."
                menu:
                    "Купить журнал за 35 ₽: как снизить стресс.":
                        if money >= 35:
                            $ money -= 35
                            $ empathy += 2
                            narr "Журнал оказался полезнее рекламы на обложке."
                        else:
                            p "35 рублей нет."
                    "Пока не покупать журнал.":
                        pass
            else:
                p "Десятки нет."

        "Купить в киоске тест на стойкость (10 ₽).":
            if money >= 10:
                $ money -= 10
                if toughness <= 3:
                    narr "Тест показывает: Вы боитесь и избегаете конфликты."
                elif toughness <= 5:
                    narr "Тест показывает: Вы в порядке."
                else:
                    narr "Тест показывает: Вас не застать врасплох, но всегда есть куда расти."
                menu:
                    "Купить журнал за 35 ₽: как повысить стойкость.":
                        if money >= 35:
                            $ money -= 35
                            $ toughness += 2
                            narr "Журнал оказался полезнее рекламы на обложке."
                        else:
                            p "35 рублей нет."
                    "Пока не покупать журнал.":
                        pass
            else:
                p "Десятки нет."

        "Ничего не покупать в киоске.":
            pass

    call hide_right from _call_hide_right_20
    call restore_main_ambience from _call_restore_main_ambience_2
    return


label day3_student_scene:
    scene expression bg_path("/streets/street_id_1")
    with dissolve
    call play_safe_dialog_music("lina-theme.mp3") from _call_play_safe_dialog_music_1
    call show_right(["student", "girl", "lina"], ["default", "idle"]) from _call_show_right_18

    narr "У остановки девушка с учебниками пытается поймать такси, но машины пролетают мимо."
    student "Извините, вы не подскажете, где тут короткий путь к университетскому общежитию?"
    p "Подскажу. Я здесь каждый двор знаю."
    narr "Паша ловит себя на внезапном желании не просто помочь, а остаться в разговоре подольше."
    student "Кстати, вы уже третий раз проходите мимо этой остановки за неделю. Я запомнила куртку."

    # Глубокий диалог: 4 правильных шага подряд.
    menu:
        "Спросить, как ее зовут, и представиться.":
            $ step1_ok = True
            p "Я Паша. А вас как зовут?"
            student "Лина."
            student "И спасибо, что не начал сразу с дешевых комплиментов."

        "Позвать на свидание.":
            $ step1_ok = False
            p "Слушай, может сходим куда-нибудь?"
            student "Мы знакомы тридцать секунд. Нет."

    if step1_ok:
        menu:
            "Помочь с маршрутом.":
                $ step2_ok = True
                p "До общаги лучше через двор с аркой и потом вдоль трамвайных путей."
                p "Там нет поворотов, не заблудишься."
                student "Большое спасибо!"

            "Про жизнь и работу.":
                $ step2_ok = False
                p "Да тут не только маршрут сложный, вся жизнь кривая."
                student "Сочувствую, но я правда спешу."

        if step2_ok:
            menu:
                "Поговорить об ее учебе и слушать внимательно.":
                    if empathy >= 2:
                        $ step3_ok = True
                    else:
                        $ step3_ok = False
                    p "На кого учишься?"
                    student "На филолога. Пишу работу по поэзии Серебряного века."
                    p "Я люблю читать, вернее любил."
                    p "Иногда, во время работы, прокручиваю лучшее."
                    p "В целом, люблю текст в стихах."
                    p "Мне близок Мандельштам: 'мы живем, под собою не чуя страны'."
                    if step3_ok:
                        student "Сильная цитата... Не ожидала услышать такое во дворе у ларька."
                    else:
                        student "Красиво, но будто выучено для эффекта. Не люблю такое."

                "Попытаться помочь с подработкой и контактами.":
                    $ step3_ok = False
                    p "Если хочешь, могу помочь с подработкой и контактами, чтобы было спокойнее с деньгами."
                    student "Спасибо. Это звучит по-человечески, но я привыкла рассчитывать на себя."

                "Сказать прямо, что у ей надо решить — идти ли в субботу." if toughness >= 4 and stress <= 3:
                    $ step3_ok = True
                    p "Лина, давай: или да, или нет. Если нет - я исчезну."
                    student "Хм... неожиданно. Это отталкивает."
                    student "Я не знаю."

            if step3_ok:
                menu:
                    "Предложить субботнюю встречу уважительно и конкретно.":
                        $ step4_ok = True
                        p "Лина, если тебе будет комфортно — давай в субботу в шесть."
                        student "Вот так уже честно. Ладно, давай попробуем."
                        $ day3_student_date_agreed = True
                        $ empathy += 1
                        $ stress = max(0, stress - 1)

                    "Давить и требовать ответ прямо сейчас.":
                        if toughness >= 3 and stress <= 3:
                            $ step4_ok = True
                            p "Идём в субботу или мы не тратим время друг друга?"
                            student "Странно, но сейчас это звучит честно. Ладно, иду."
                            $ day3_student_date_agreed = True
                            $ toughness += 1
                        else:
                            $ step4_ok = False
                            p "Ну давай быстро решай: да или нет."
                            student "Точно нет. Удачи."
                            $ empathy -= 1

    if not day3_student_date_agreed:
        narr "Лина кивает на прощание и уходит к остановке."
        p "Поторопился. Снова сделал из разговора проверку, а не встречу."

    call hide_right from _call_hide_right_21
    call restore_main_ambience from _call_restore_main_ambience_3
    return


label day3_lost_package_debt_branch:
    if not day2_lost_roma_package:
        return

    scene expression bg_path("/entrances/entrance_id_1")
    with dissolve
    call show_right(["debt", "gena"], ["default", "idle"]) from _call_show_right_19

    narr "У подъезда в тени курит широкоплечий мужчина в темной дубленке."
    debt "Паша? Я Гена. По Роминому вопросу."
    p "Я... понял."
    debt "Ты потерял его пакет. Это дорого."
    debt "Но есть вариант отработать. Едешь на заброшку. Там цель."
    debt "Сделаешь — долг закрыт."

    menu:
        "Согласиться.":
            p "Ладно. Поехали."
            call pass_time(30) from _call_pass_time_4
            call day3_abandoned_choice from _call_day3_abandoned_choice

        "Отказаться.":
            p "Нет. Я не пойду на такое."
            debt "Тогда плати иначе."
            $ money = max(0, money - 50)
            $ empathy = max(0, empathy - 2)
            $ toughness = max(0, toughness - 2)
            call stress_up(2) from _call_stress_up_15
            debt "Запомни: сегодня ты выбрал страх, а не долг."

    call hide_right from _call_hide_right_22
    return


label day3_abandoned_choice:
    scene expression day1_image("/abandoned/abandoned_id_1")
    with dissolve

    $ known_neutral = renpy.random.choice([
        "oldw", "igor", "lesha", "dvornik", "librarian", "student"
    ])
    $ day3_abandoned_target = known_neutral

    if known_neutral == "oldw":
        call show_right(["oldw", "oldwoman", "babka"], ["default", "idle"]) from _call_show_right_20
        narr "В проеме стоит Тамара Петровна, кутаясь в старый платок."
        oldw "Сынок?.. Почему у тебя в руках оружие?"
    elif known_neutral == "igor":
        call show_right(["boy", "guy", "igor"], ["default", "idle"]) from _call_show_right_21
        narr "У стены мнется Игорь, бледный, как мел."
        guy "Мы же друзья..."
    elif known_neutral == "lesha":
        call show_right(["lesha", "guy"], ["default", "idle"]) from _call_show_right_22
        narr "У ржавой двери стоит Лёша, руки подняты."
        lesha "Слушай, я вообще не при делах. Меня сюда позвали на 'разговор'."
    elif known_neutral == "dvornik":
        call show_right(["dvornik", "oldman"], ["default", "idle"]) from _call_show_right_23
        narr "Под аварийной лампой узнается Семёныч."
        dvornik "Вот до чего доводит страх, Паша."
    elif known_neutral == "librarian":
        call show_right(["librarian", "man"], ["default", "idle"]) from _call_show_right_24
        narr "На бетонном блоке сидит Марат, библиотекарь, и смотрит спокойно."
        librarian "Выходит, вопрос о правде и лжи был не академический."
    else:
        call show_right(["student", "girl", "lina"], ["default", "idle"]) from _call_show_right_25
        narr "В свете разбитого фонаря — Лина, испуганная и злая одновременно."
        student "Это что, розыгрыш? Убери пистолет!"

    menu:
        "Выстрелить.":
            narr "Палец сам находит спуск. Грохот отдается в ребрах."
            scene expression bg_path("/abandoned/abandoned_id_1")
            with vpunch
            call show_right(["cop", "klimov", "police"], ["default", "idle"]) from _call_show_right_26
            cop "Оружие на землю!"
            p "Я..."
            cop "Поздно."
            jump ending_prison

        "Опустить пистолет и уйти домой.":
            p "Нет. Не так."
            if known_neutral == "oldw":
                oldw "Только один из двух останется."
            elif known_neutral == "igor":
                guy "Только один из двух останется."
            elif known_neutral == "lesha":
                lesha "Только один из двух останется."
            elif known_neutral == "dvornik":
                dvornik "Только один из двух останется."
            elif known_neutral == "librarian":
                librarian "Только один из двух останется."
            else:
                student "Только один из двух останется."
            p "Поясни. Кто из двух?"
            narr "В ответ — молчание."
            narr "Ты разворачиваешься и идешь к выходу, слыша за спиной только собственное дыхание."
            p "Мне это привиделось? Тогда кто цель? Может я..."
            call stress_up(1) from _call_stress_up_16

    call hide_right from _call_hide_right_23
    return
