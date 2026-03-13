# Day 4

label day_4:
    call ensure_main_ambience from _call_ensure_main_ambience_3
    call init_day_clock(0, 0) from _call_init_day_clock_4

    scene black
    with dissolve
    narr "Четверг. 00:00. Паша не спит и смотрит в потолок, где тени похожи на карту чужого города."
    p "Кажется, я давно живу не днями, а обрывками между звонком в цехе и дверью подъезда."
    p "Что вообще происходит на фабрике? Что именно я там делаю?"
    scene expression bg_path("start-game_id_4")
    p "Почему каждую смену помню как в тумане, будто кто-то вырезает из памяти часы целиком."


    call pass_time(120) from _call_pass_time_5
    narr "02:00. Из-за двери слышится медленное царапанье. Ровное, терпеливое, почти человеческое."

    menu:
        "Пойти смотреть в глазок.":
            $ day4_night_checked_door = True
            call day4_night_peephole from _call_day4_night_peephole

        "Попытаться уснуть, не вставая.":
            p "Если встану — только сильнее себя накручу. Надо переждать до утра."
            call stress_up(1) from _call_stress_up_17
            call init_day_clock(6, 30) from _call_init_day_clock_5
            narr "06:30. Сон был рваным и коротким, но будильник все равно возвращает тебя в тело."

    call day4_morning_route from _call_day4_morning_route
    call day4_work_shift from _call_day4_work_shift
    call day4_evening_route from _call_day4_evening_route

    call day4_final_homecoming from _call_day4_final_homecoming

    call stop_day_clock from _call_stop_day_clock_3
    $ day += 1
    jump week_loop


label day4_night_peephole:
    scene expression bg_path("/entrances/entrance_id_3")
    with dissolve

    narr "Паша босиком подходит к двери и прижимается к глазку."
    narr "На площадке пусто: пыльная лампа, перила, облупленная краска."
    $ stare_minutes = 0

    while True:
        menu:
            "Ничего не делать, просто смотреть дальше.":
                $ stare_minutes += 1
                call pass_time(1) from _call_pass_time_6
                if stare_minutes >= 3:
                    call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_2
                    scene expression bg_path("/entrances/dvernoy_glazok")
                    narr "На третьей минуте в глазке резко появляется чужой глаз — слишком близко, слишком неподвижно."
                    narr "Царапанье обрывается."
                    p "Кто там?!"
                    narr "Шепот прямо по ту сторону двери:"
                    narr "'Ты каждый вечер выходишь, чтобы вернуться. Когда выйдешь, чтобы уйти?'"
                    $ day4_peephole_event_seen = True
                    $ day4_faceless_phrase_heard = True
                    call stress_up(2) from _call_stress_up_18
                    menu:
                        "Отпрянуть от двери.":
                            narr "Секунду спустя площадка снова пуста."
                        "Открыть дверь рывком.":
                            narr "За дверью никого."
                    call restore_main_ambience from _call_restore_main_ambience_4
                    call init_day_clock(5, 50) from _call_init_day_clock_6
                    narr "Остаток ночи проходит без сна."
                    return
                else:
                    narr "Пока ничего. Только собственное дыхание, усиленное глазком."

            "Открыть дверь сразу.":
                narr "Дверь распахивается в пустой подъезд. На ступени — влажный след, как от рабочего ботинка."
                call stress_up(1) from _call_stress_up_19
                call init_day_clock(5, 40) from _call_init_day_clock_7
                return

            "Отойти и лечь обратно.":
                p "Хватит. Иначе к утру разнесет голову."
                call init_day_clock(6, 30) from _call_init_day_clock_8
                return


label day4_morning_route:
    scene expression bg_path("/streets/street_id_2")
    with dissolve
    narr "Утро серое и жидкое. Паша идет к остановке, потом пешком вдоль промзоны — на работу."

    if day3_librarian_factory_phrase_heard or day4_faceless_phrase_heard:
        p "Когда я последний раз выходил из дома, чтобы прийти на фабрику?"
        p "Странно: вопрос простой, а внутри от него холодно."

    call show_right(["dvornik", "oldman"], ["default", "idle"]) from _call_show_right_27
    dvornik "Рано сегодня. Лицо как после трех смен подряд."
    if day3_abandoned_target == "dvornik":
        p "Семёныч... на секунду показалось, что я вчера видел тебя в очень плохом месте."
        dvornik "Иногда мы видим людей не там, где они есть, а там, где нам страшно."
    menu:
        "Спросить, как часто Семёныч вообще меня видит.":
            p "Семёныч, чисто из интереса: ты меня часто замечаешь?"
            dvornik "Чаще, чем ты думаешь. Будто один и тот же человек проходит мимо разными походками."
            call stress_up(1) from _call_stress_up_20

        "Отмахнуться и идти дальше.":
            p "После ночи просто голова гудит."
            dvornik "Береги голову. Она у тебя теперь рабочий инструмент."
    call hide_right from _call_hide_right_24

    call day4_pharmacy_scene from _call_day4_pharmacy_scene

    scene expression bg_path("/buildings/factory_exit_id_2")
    with dissolve
    narr "У проходной Пашу догоняет Игорь, постоянно оглядываясь на пустую арку."
    call show_right(["boy", "guy", "igor"], ["default", "idle"]) from _call_show_right_28
    if day3_abandoned_target == "igor":
        p "Игорь, у меня дикий вопрос. Ты вчера ночью был на заброшке?"
        guy "Нет..."
    guy "Паш, что-то случилось?"
    menu:
        "Признаться, что слышал что-то ночью.":
            p "Слышал ночью звук. И это было не похоже на обычный страх."
            guy "Значит, я не один с этим."
            $ empathy += 1

        "Сделать вид, что все нормально.":
            p "Нет. И тебе совет: меньше смотри по сторонам ночью."
            $ toughness += 1
    call hide_right from _call_hide_right_25

    call pass_time(35) from _call_pass_time_7
    return


label day4_pharmacy_scene:
    scene expression bg_path("/buildings/pharmacy")
    with dissolve
    narr "Аптека выглядит лучше половины города. Горит красный крест на белом фоне."
    narr "Почему белый пластырь не закрывает красную рану? Не важно."

    menu:
        "Зайти в аптеку за успокоительным.":
            narr "Внутри пахнет спиртом, мятой и мокрыми пальто."
            menu:
                "Купить успокоительное за 12 ₽.":
                    if money >= 12:
                        $ money -= 12
                        call day4_take_item("успокоительное") from _call_day4_take_item
                        p "Пусть будет. На всякий случай."
                    else:
                        p "Денег не хватает."

                "Не покупать ничего.":
                    p "Ладно, переживу так."

        "Не заходить и идти дальше.":
            pass

    return


label day4_take_item(item_name):
    if item_name in inventory:
        return
    call add_item(item_name) from _call_add_item_3
    return


label day4_work_shift:
    scene expression bg_path("start-game_id_4")
    with dissolve
    narr "Смена тянется вязко: станки воют, а время будто идет рывками."
    p "Опять провалы... словно куски дня кто-то монтирует без меня."
    narr "В конце смены Паша ловит себя на том, что не помнит, как дошел до раздевалки."

    call init_day_clock(20, 30) from _call_init_day_clock_9
    narr "20:30. Турникет проходной щелкает, и холодный воздух бьет в лицо."
    call apply_shift_bonus from _call_apply_shift_bonus_2
    return


label day4_evening_route:
    scene expression bg_path("/streets/street_id_1")
    with dissolve

    if day3_student_date_agreed:
        narr "У остановки Паша замечает Лину: она кутается в шарф и узнает его издалека."
        call play_safe_dialog_music("student") from _call_play_safe_dialog_music_2
        call show_right(["student", "girl", "lina"], ["default", "idle"]) from _call_show_right_29
        if day3_abandoned_target == "student":
            p "Лина... странный вопрос. Ты вчера ночью была у заброшки?"
            student "Нет. И, если честно, звучит так, будто тебе нужно выспаться."
        student "Паша, ты хоть не забыл про субботу?"
        p "Не забыл."
        call hide_right from _call_hide_right_26
        call restore_main_ambience from _call_restore_main_ambience_5

    call day4_roma_scene from _call_day4_roma_scene

    scene expression bg_path("/buildings/kiosk")
    with dissolve
    narr "У киоска под желтым фонарем стоит Марат и смотрит на закрытые витрины, как на текст с пропущенными строчками."
    call show_right(["librarian", "man"], ["default", "idle"]) from _call_show_right_30
    if day3_abandoned_target == "librarian":
        p "Марат, я тебя вчера видел... там, где ты не должен был быть."
        librarian "Мы часто встречаем знакомых в собственном страхе."
    librarian "Четверг проверяет человека на память. Что он помнит о себе, а что — только о роли."
    menu:
        "Спросить, можно ли забыть себя окончательно.":
            p "Марат, а можно забыть себя и жить по инерции?"
            librarian "Можно. Обычно это называется 'удобный сотрудник'."
            $ empathy += 1

        "Попросить его не давить философией.":
            p "Давай сегодня без глубины. И так штормит."
            librarian "Без глубины тоже тонут. Просто медленнее."
            $ stress += 1

    call hide_right from _call_hide_right_27

    if day3_librarian_factory_phrase_heard or day4_faceless_phrase_heard:
        menu:
            "Пойти домой как обычно.":
                p "Домой. Сегодня без экспериментов."

            "Пойти не домой, а обратно к фабрике.":
                call day4_factory_detour from _call_day4_factory_detour

    call day4_empty_world_walk from _call_day4_empty_world_walk
    return


label day4_roma_scene:
    narr "У табачного киоска Паше преграждает дорогу Рома: пальцы в перчатках, взгляд беспокойный."
    call show_right(["broker", "roma", "temshik"], ["default", "idle"]) from _call_show_right_31
    broker "Паша, стой. Ты Гену не видел? Коллектор на связь не выходит с ночи."
    broker "Здоровый, в темной дубленке, голос как наждак. Не заметить трудно."

    menu:
        "Сказать, что не видел Гену.":
            p "Нет, не попадался."
            broker "Плохо. Когда такие пропадают — это чей-то плохой день."

        "Сказать, что видел похожего человека у подъезда.":
            p "Похожий крутился у подъезда. Нервный, дерганый."
            broker "Хм. Значит жив и суетится. Уже лучше. Держи пятёрик."
            $ money += 5

        "Съязвить, что такие как Гена сами кого угодно найдут.":
            p "Гена? Он сам людей находит быстрее, чем люди его."
            broker "Острый язык у тебя. Смотри, не обрежься."
            call stress_up(1) from _call_stress_up_21

    broker "Есть еще темка. Найди карманника Лёню и забери у него серый футляр."
    broker "Он должен был передать мне вещь и исчез. Заберешь футляр — получишь 40 ₽."

    menu:
        "Взяться за поиски Лёни.":
            p "Где искать?"
            broker "Киоск, подворотни, остановка. Он любит толпу и быстрые руки."
            call hide_right from _call_hide_right_28
            call day4_find_pickpocket from _call_day4_find_pickpocket

        "Отказаться.":
            p "Сегодня нет. Хватит с меня чужих дел."
            broker "Как знаешь."
            call hide_right from _call_hide_right_29

    return


label day4_find_pickpocket:
    scene expression bg_path("/courtyards/yard_id_3")
    with dissolve
    narr "В арке мелькает знакомая сутулая фигура: Лёня оглядывает карманы прохожих."
    call show_right(["thief", "lenya"], ["default", "idle"]) from _call_show_right_32

    thief "О, знакомое лицо с тяжелым взглядом. Чего надо?"
    p "Серый футляр. Он не твой."

    menu:
        "Запугать и потребовать вернуть футляр.":
            if toughness >= 3:
                p "Лёня, это уже мой футляр."
                thief "Ладно-ладно..."
                call day4_take_item("серый футляр") from _call_day4_take_item_1
                $ toughness += 1
            else:
                narr "Карманник преобразился в лице, подобрел."
                thief "Паша, дружище, зачем ты такое говоришь?"
                thief "Я купил футляр в ларьке, возвращаюсь домой, а тут ты, не хорошо."
                narr "Лёня отталкивает Пашу и уходит. Вам не хватает смелости побежать за ним."
                $ toughness -= 1
                call stress_up(1) from _call_stress_up_22
                call hide_right from _call_hide_right_30
                return

        "Предложить выкупить футляр за 15 ₽.":
            if money >= 15:
                $ money -= 15
                thief "Вот это по-деловому."
                call day4_take_item("серый футляр") from _call_day4_take_item_2
                $ toughness -= 1
                $ empathy += 1
            else:
                p "Не хватает."
                thief "Тогда и разговора нет."
                call stress_up(1) from _call_stress_up_23
                call hide_right from _call_hide_right_31
                return

        "Схватить Лёню за куртку.":
            narr "Лёня вырывается, и вы оба падаете на мокрый асфальт."
            if toughness >= 2:
                narr "Ты находишь футляр и отходишь первым."
                call day4_take_item("серый футляр") from _call_day4_take_item_3
            else:
                thief "Зря полез."
                if money > 0:
                    $ loss = min(money, 10)
                    $ money -= loss
                    narr "В суматохе пропало [loss] ₽."
                call hide_right from _call_hide_right_32
                return

    thief "Все, свободен?"
    call hide_right from _call_hide_right_33

    scene expression bg_path("/streets/street_id_1")
    with dissolve
    call show_right(["broker", "roma", "temshik"], ["default", "idle"]) from _call_show_right_33
    broker "Ну?"

    if "серый футляр" in inventory:
        call remove_item("серый футляр") from _call_remove_item_4
        broker "Красиво. Держи 40 ₽."
        $ money += 40
        menu:
            "Спросить, что было в футляре.":
                p "Что там вообще?"
                broker "Что-то за что не жалко отдать 40 рублей."
                broker "Но я скажу тебе кое-что."
                broker "Братки весточку передали: менты тебя пасут."
                broker "Выйдут на меня - ты труп. Не лажай, Пашок."
            "Не задавать вопросов.":
                p "Спасибо."
    else:
        broker "Пустой пришел? Значит и разговор с тобой пустой."

    call hide_right from _call_hide_right_34
    return


label day4_factory_detour:
    $ day4_frozen_minutes = game_minutes
    $ day4_time_frozen = True
    call stop_day_clock from _call_stop_day_clock_4

    p "Нет. Сегодня я пойду не домой. Я пойду туда, откуда каждый день 'возвращаюсь'."
    narr "Ты разворачиваешься к фабрике."
    narr "Стрелки часов больше не двигаются."

    scene expression bg_path("/courtyards/yard_id_5")
    with dissolve
    call switch_to_anomaly_ambience from _call_switch_to_anomaly_ambience
    call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_3
    call show_right(["blink", "man"], ["default", "idle"]) from _call_show_right_34
    blink "Решил идти против маршрута?"

    if "успокоительное" in inventory:
        menu:
            "Принять успокоительное прямо сейчас.":
                call remove_item("успокоительное") from _call_remove_item_5
                p "Мне нужно, чтобы руки не дрожали."
                blink "Ха... ха-ха... человек лечит страх таблеткой, а не правдой."
                narr "Аномальный неожиданно смеется — глухо и надсадно."
                $ stress -= 1

            "Не принимать ничего.":
                p "Обойдусь."
                call stress_up(1) from _call_stress_up_24
                $ toughness += 1
    else:
        p "Мне и так хватит."

    blink "Иди. Там тебя ожидают твои стены."
    call hide_right from _call_hide_right_35

    call day4_factory_reveal from _call_day4_factory_reveal
    call restore_main_ambience from _call_restore_main_ambience_6
    return


label day4_factory_reveal:
    scene expression bg_path("/buildings/factory_exit_id_2")
    with dissolve
    narr "Проходная открыта, как будто тебя здесь ждали."
    narr "Ты заходишь внутрь — и замираешь."

    scene expression bg_path("/entrances/entrance_id_3")
    with dissolve
    narr "Вместо цеха — твой подъезд. Те же ступени. Те же трещины на стене."
    p "Нет... это не может быть."

    scene expression bg_path("/entrances/my_room")
    with dissolve
    narr "Ты поднимаешься выше и открываешь дверь 'раздевалки'."
    narr "За дверью — твоя квартира. Твой стол. Твоя кружка."
    p "Я пришел на фабрику... и зашел домой?"
    narr "На полке в прихожей пылится детская игрушка из твоей квартиры."
    narr "Ты не можешь вспомнить, всегда ли у нее не было лица — или это случилось только сейчас."

    call stress_up(2) from _call_stress_up_25

    if toughness >= 4:
        p "Маршрут от фабрики до дома один."
        p "Если маршрут один, почему я прохожу через разные дворы и улицы."
        p "А если я куда-то ещё захожу..."
        $ day4_split_personality_revealed = True

    scene expression bg_path("/entrances/entrance_id_1")
    with dissolve
    narr "Ты выходишь из квартиры и у подъезда встречаешь дворника."
    call show_right(["dvornik", "oldman"], ["default", "idle"]) from _call_show_right_35
    dvornik "Я уже домой собирался, а ты снова тут."

    if day4_split_personality_revealed:
        p "Семёныч... как часто ты меня видишь за день?"
        dvornik "Не меньше четырех раз."
        dvornik "Утром один человек, в обед будто другой, вечером третий, ночью снова первый."
    else:
        p "Семёныч, это сон?"
        dvornik "Хотел бы я сказать, что да."

    dvornik "Может, у тебя не один маршрут. Может, и не один ты."
    call hide_right from _call_hide_right_36

    p "Каждый раз, когда 'я' иду на работу... кто-то другой, возможно, идет домой."
    p "А к концу смены возвращается к проходной, будто ничего не было."
    $ day4_split_personality_revealed = True

    return


label day4_empty_world_walk:
    scene expression bg_path("/courtyards/yard_id_2")
    with dissolve
    narr "Ты решаешь пройтись по всем знакомым точкам — проверить, не врёт ли город."

    scene expression bg_path("/garages/garage_id_2")
    with dissolve
    narr "Гаражи пусты. Ни Санька, ни голосов, ни музыки из старого приемника."

    scene expression bg_path("/streets/street_id_2")
    with dissolve
    narr "Остановка пуста. Даже расписание будто выцвело за одну ночь."

    scene expression bg_path("/buildings/magazine_id_1")
    with dissolve
    narr "Киоск, внутри никого. Такое бывает?"

    scene expression bg_path("/abandoned/abandoned_id_1")
    with dissolve
    narr "На заброшке тишина такая, что слышно, как кровь стучит в висках."

    scene expression bg_path("/courtyards/yard_id_4")
    with dissolve
    narr "Пусто. Мир будто вычел из себя людей и оставил только декорации."

    p "Человек без лица..."
    p "Если его никто не видел в лицо, если у него нет черт..."
    p "Что, если это я и есть?"
    call stress_up(1) from _call_stress_up_26
    return


label day4_final_homecoming:
    scene expression bg_path("/entrances/entrance_id_1")
    with dissolve

    if day4_time_frozen:
        $ fh = (day4_frozen_minutes // 60) % 24
        $ fm = day4_frozen_minutes % 60
        call init_day_clock(fh, fm) from _call_init_day_clock_10
        $ day4_time_frozen = False
        narr "Как только ты подходишь к своему подъезду, стрелки часов снова начинают идти."

    call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_4
    call show_right(["thin", "anomaly_tall"], ["default", "idle"]) from _call_show_right_36
    narr "У лестницы уже стоит высокий худой. Голова дергается рывками, как у сломанной куклы."
    thin "Пппп-очему тт-ы не доомммаааааа..."
    thin "Ттттвой дддом ннне тттам..."
    narr "Его челюсть выворачивается на невозможный угол, и он с визгом бросается прямо на тебя."
    narr "Ты рефлекторно отскакиваешь в сторону."
    narr "Фигура проходит сквозь тебя, как сквозняк, и исчезает."
    call stress_up(1) from _call_stress_up_27

    call hide_right from _call_hide_right_37
    call restore_main_ambience from _call_restore_main_ambience_7

    scene expression bg_path("/entrances/entrance_id_3")
    with dissolve
    narr "Паша поднимается к двери квартиры и долго держит ладонь на холодной ручке."
    p "Что я делаю в тех часах, которых не помню?"
    p "Если я сам себе человек без лица... сколько меня вообще?"
    narr "Он заходит домой. Дверь закрывается мягко, почти без звука."
    scene black
    with fade
    narr "Ночь с четверга на пятницу тянется без сна. К утру ты уже знаешь: следующая смена не будет обычной."
    return
