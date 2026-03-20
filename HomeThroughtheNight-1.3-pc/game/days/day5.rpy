# Day 5

label day_5:
    call ensure_main_ambience from _call_ensure_main_ambience_4
    call init_day_clock(18, 30) from _call_init_day_clock_11

    scene expression bg_path("start-game_id_5")
    with dissolve
    narr "Пятница. Паша засыпает на лавке у проходной и проваливается в тяжелый сон."
    narr "Во сне он снова идет дорогой четверга: фабрика, подъезд, дверь, снова фабрика."
    if day4_split_personality_revealed:
        p "Если это правда... то вчера на фабрике я вошел в собственную квартиру."
    else:
        p "Четверг как пятно на пленке. Вроде помню, а будто не со мной было."

    scene expression bg_path("/buildings/factory_exit_id_2")
    with dissolve
    narr "19:30. Смена закончилась раньше обычного, и Пашу отпустили домой."
    narr "Улица непривычно пустая."
    p "Дел сегодня куча. И времени как будто нет вовсе."

    call day5_street_dialogs from _call_day5_street_dialogs

    if day4_split_personality_revealed:
        menu:
            "Снова проверить путь через фабрику.":
                call day5_factory_shortcut from _call_day5_factory_shortcut
            "Идти через город, как обычно.":
                p "Нет, сегодня без рывков. Пойду по улицам."
    call day5_kiosk_and_beer from _call_day5_kiosk_and_beer
    call day5_oldwoman_scene from _call_day5_oldwoman_scene
    call day5_entrance_smile from _call_day5_entrance_smile
    call day5_final_eval from _call_day5_final_eval

    call stop_day_clock from _call_stop_day_clock_5
    $ day += 1
    jump week_loop


label day5_street_dialogs:
    scene expression bg_path("/streets/street_id_1")
    with dissolve

    call show_right(["lesha", "guy"], ["default", "idle"]) from _call_show_right_37
    lesha "Слышал? Новыя объявления о пропаже."
    lesha "И Марат из библиотеки тоже как сквозь землю."
    menu:
        "Спросить, кто еще это знает.":
            p "Кто подтвердил?"
            lesha "Люди шепчутся на остановке. Полиция уже крутится у киоска."
            $ empathy += 1
        "Сделать вид, что тебе все равно.":
            p "Меня это не касается."
            lesha "Сегодня не касается. Завтра — кто знает."
            call stress_up(1) from _call_stress_up_28
    call hide_right from _call_hide_right_38

    scene expression bg_path("/buildings/pharmacy")
    with dissolve
    narr "У аптеки Паша замечает Лину. Она стоит под вывеской и смотрит в землю."
    p "Последний цвет."
    narr "Ты проходишь мимо. В этот вечер вы не говорите ни слова."

    scene expression bg_path("/courtyards/yard_id_3")
    with dissolve
    call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_5
    call show_right("neck", ["default", "idle"]) from _call_show_right_38
    neck "Извините... вы не подскажете, где здесь выход?"
    p "Мы знакомы?"
    neck "Нет. В первый раз вас вижу."
    narr "Лицо женщины дергается и расплывается, будто мокрая краска."
    if "фонарик" in inventory:
        p "Стой."
        narr "Ты светишь фонариком в лицо аномальной. Под кожей — серые пятна, как у мертвеца."
        $ day5_understood_death_link = True
    call hide_right from _call_hide_right_39
    call restore_main_ambience from _call_restore_main_ambience_8

    return


label day5_factory_shortcut:
    $ day5_before_factory = game_minutes
    scene expression bg_path("/buildings/factory_exit_id_2")
    with dissolve
    p "Если я уже делал это вчера, то смогу и сейчас."

    if renpy.random.randint(0, 1) == 0:
        call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_6
        call show_right(["thin", "anomaly_tall"], ["default", "idle"]) from _call_show_right_39
        thin "Д-д-ом не там..."
    else:
        call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_7
        call show_right(["blink", "man"], ["default", "idle"]) from _call_show_right_40
        blink "Ты опять ищешь короткий путь?"

    if toughness <= 5:
        call stress_up(1) from _call_stress_up_29
    else:
        p "Не сегодня."

    narr "Ты открываешь дверь проходной."
    scene expression bg_path("/entrances/entrance_id_3")
    with dissolve
    narr "За дверью сразу лестничная площадка твоего дома."
    p "На моих часах прошло меньше 5 минут, я не мог оказаться здесь так быстро."
    if day4_split_personality_revealed:
        p "Что если это уже происходило."
        p "Значит, одна из моих личностей прячет свое присутствие, пока я проваливаюсь в пустоты памяти."
        p "Эти аномальные, эти пропажи людей, другая личность, всё связано со мной."
        $ day5_understood_death_link = True
    call hide_right from _call_hide_right_40
    call restore_main_ambience from _call_restore_main_ambience_9
    $ day5_quests_done += 1
    return


label day5_kiosk_and_beer:
    scene expression bg_path("/buildings/kiosk")
    with dissolve

    menu:
        "Проверить киоск: последний шанс найти Марата.":
            narr "Киоск открыт. На кривом гвозде висит свежий журнал: 'Как справляться со стрессом'."
            menu:
                "Купить журнал за 40 ₽." if money >= 40:
                    $ money -= 40
                    $ old_stress = stress
                    $ stress = max(0, stress // 2)
                    $ toughness += 1
                    narr "Ты читаешь пару страниц прямо у киоска. Дыхание выравнивается."
                    if stress < old_stress:
                        narr "Внутри становится заметно тише. Нервное напряжение отступает, стойкость растёт."
                    else:
                        narr "Становится чуть легче держать себя в руках."
                    $ day5_quests_done += 1
                "Не покупать.":
                    p "Потом."
        "Сразу идти к ларьку, где договорились пить пиво." if day1_agreed_beer and not day4_split_personality_revealed:
            p "Ладно."
        "Пропустить киоск.":
            p "Ладно."

    if day1_agreed_beer and not day4_split_personality_revealed:
        call day5_beer_wait from _call_day5_beer_wait

    scene expression bg_path("/streets/street_id_2")
    with dissolve
    call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_8
    call show_right("/librarian/teeth") from _call_show_right_41
    teeth "Время пошло вспять."
    p "Марат?"
    teeth "Не знаю тебя. Первый раз вижу."
    if "брошюра Марата" in inventory:
        p "Марат писал: 'Личность может не помнить маршруты другой личности'."
        p "Или это не личности... а люди, которые уже умерли."
        $ day5_understood_death_link = True
        $ day5_quests_done += 1
    call hide_right from _call_hide_right_41
    call restore_main_ambience from _call_restore_main_ambience_10
    return


label day5_beer_wait:
    $ game_minutes = max(game_minutes, 21 * 60)
    narr "Около 21:00 ты приходишь к ларьку. Игоря нет."

    while game_minutes < 21 * 60 + 30:
        menu:
            "Подождать еще 10 минут.":
                call pass_time(10) from _call_pass_time_8
                $ day5_waited_for_boy = True
                narr "Проходит еще десять минут. Улица пустеет."
            "Уйти, пока не стало поздно.":
                p "Хватит."
                return

    call day5_klimov_scene from _call_day5_klimov_scene
    return


label day5_klimov_scene:
    scene expression bg_path("/buildings/kiosk")
    with dissolve
    call show_right(["cop", "klimov", "police"], ["default", "idle"]) from _call_show_right_42
    cop "Кого ждем, Паша?"
    p "..."

    menu:
        "Сказать правду: жду Игоря у пива.":
            p "Игоря жду. Мы собирались выпить пива."
            cop "Ублюдок, я найду доказательства."
            if toughness >= 7:
                p "Полегче с тоном. Почему ты так со мной разговариваешь?"
                cop "Потому что за неделю пропали двое. Был свидетель: видел тебя рядом с местами исчезновений."
                cop "И свидетель тоже пропал."
            cop "Я засажу тебя за решетку."
            cop "Только не понимаю, зачем ты пришел на встречу, если мочканул того бедолагу. Скройся с глаз моих!"
            $ day5_police_suspicion = True

        "Соврать, что просто проходил мимо.":
            p "Никого. Просто шел домой."
            cop "Врешь. Но пока иди."
            call stress_up(1) from _call_stress_up_30
            $ day5_police_suspicion = True

        "Показать пакет Ромы как 'доказательство' своих дел." if "пакет Ромы" in inventory:
            p "У меня был курьерский пакет Ромы, спроси у него."
            cop "Темщик пропал. И пакет тебя не обеляет."
            $ day5_police_suspicion = True
            call stress_up(1) from _call_stress_up_31

    call hide_right from _call_hide_right_42
    return


label day5_oldwoman_scene:
    scene expression bg_path("/courtyards/yard_id_4")
    with dissolve
    call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_9

    menu:
        "Зайти к бабке.":
            call show_right(["oldw", "oldwoman", "babka"], ["default", "idle"]) from _call_show_right_43
            oldw "Внучок, я давно тебя простила, ступай."
            $ day5_oldwoman_hint = True
            menu:
                "Попросить прощения." if toughness > 3:
                    p "Прости меня... за всё, что я не успел исправить."
                    oldw "Память лечит не сразу, но ты уже начал."
                    $ empathy += 1
                "Это был не я.":
                    p "Это был не я."
                    oldw "Я знаю. Но тебе всё равно жить с этим."
            call hide_right from _call_hide_right_43
            $ empathy += 1
            $ day5_quests_done += 1
        "Не заходить.":
            p "Не сейчас."
    call restore_main_ambience from _call_restore_main_ambience_11
    return


label day5_entrance_smile:
    scene expression bg_path("/entrances/entrance_id_1")
    with dissolve
    call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_10
    call show_right(["smile", "boy"], "smile") from _call_show_right_44
    narr "У двери подъезда молча стоит улыбающийся мужчина. В его чертах ты узнаешь искаженного Игоря."

    menu:
        "Молча пройти мимо.":
            call stress_up(1) from _call_stress_up_32
        "Попросить прощения." if toughness > 3:
            p "Прости."
            if empathy >= 5:
                smile "Я знаю. Жалко пиво выпил не с Тобой."
                $ day5_understood_death_link = True
                $ day5_quests_done += 1
            else:
                narr "Улыбка становится шире, но ответа нет."
        "Это был не я.":
            p "Это был не я."
            narr "Улыбка не меняется, будто он и без слов это знает."

    call hide_right from _call_hide_right_44
    call restore_main_ambience from _call_restore_main_ambience_12
    return


label day5_final_eval:
    if day5_police_suspicion and (day5_understood_death_link and stress >= 7):
        scene black
        with fade
        narr "Ночью в дверь стучат. Климов приходит с понятыми и постановлением на обыск."
        narr "Под кроватью находят улику, которой ты сам не можешь объяснить происхождение."
        $ day5_arrested = True
        jump ending_prison

    if day5_understood_death_link and stress >= 6 and toughness <= 2:
        jump ending_suicide

    if day4_split_personality_revealed and completed_quest_ratio() >= 0.3:
        if toughness >= 3 and day5_understood_death_link:
            jump ending_blood_tools
        else:
            jump ending_faceless_function

    if empathy <= 3:
        jump ending_faceless_function

    if money >= 240 and day4_split_personality_revealed:
        jump ending_clinic

    if not day5_understood_death_link:
        jump ending_faceless_function
