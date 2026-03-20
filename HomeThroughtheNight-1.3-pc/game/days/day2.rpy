# Day 2

label day_2:
    call ensure_main_ambience from _call_ensure_main_ambience_1
    call init_day_clock(20, 30) from _call_init_day_clock_1

    scene black
    with dissolve
    narr "Перед выходом Паша проваливается в тяжелый, рваный сон, будто тонет в собственной тени."
    p "Депрессия похожа на подвал без лестницы: ты помнишь, что наверху есть свет, но каждый шаг вниз звучит убедительнее надежды."
    p "Я читал, что отчаяние питается тишиной, однако самые страшные его слова всегда произносит мой собственный голос."
    p "Если человек — это сумма прожитых смыслов, то мне нужно срочно научиться складывать себя заново."

    scene expression bg_path("start-game_id_2")
    with dissolve

    narr "Вторник. Паша снова выходит из цеха в сырой вечер."
    narr "У проходной рабочие переговариваются вполголоса: в районе снова пропал человек, и каждый спешит домой до темноты."
    call apply_shift_bonus from _call_apply_shift_bonus
    p "Сорок минут дороги... и опять то же самое завтра."
    p "Иногда кажется, что я живу не жизнь, а сменный график."

    call day2_random_returns from _call_day2_random_returns
    call day2_lost_keys_scene from _call_day2_lost_keys_scene
    call day2_hard_money_quest from _call_day2_hard_money_quest
    call day2_finish from _call_day2_finish

    $ day += 1
    jump week_loop

label day2_random_returns:
    $ returns = renpy.random.sample(["sanek", "oldw", "igor"], 1)

    if "sanek" in returns:
        scene expression bg_path("/buildings/factory_exit_id_2")
        with dissolve
        call show_right(["gopnik", "sanek"], ["default", "idle"]) from _call_show_right_3
        gop "Пашка, тихий будь сегодня. Район на нервах."
        p "Да я и так тише воды."
        call hide_right from _call_hide_right_3

    if "oldw" in returns:
        scene expression bg_path("/buildings/factory_exit_id_2")
        with dissolve
        call show_right(["oldw", "oldwoman", "babka"], ["default", "idle"]) from _call_show_right_4
        oldw "Опять ты. Держись правой стороны — там светлее."
        p "Спасибо, Тамара Петровна."
        call hide_right from _call_hide_right_4

    return

label day2_lost_keys_scene:
    scene expression bg_path("/entrances/entrance_id_2")
    with dissolve

    call show_right(["lesha", "guy"], ["default", "idle"]) from _call_show_right_5
    lesha "Мужик, выручай. Ключи где-то тут выронил."
    lesha "Дома ребенок один, я уже весь двор обшарил."

    if "фонарик" in inventory:
        menu:
            "Посветить фонариком и поискать ключи.":
                p "Ладно, показывай, где ходил."
                narr "Свет фонарика выхватывает связку ключей под влажной лавкой."
                menu:
                    "Отдать ключи Лёше.":
                        $ day2_lost_keys_resolved = True
                        p "Держи. В следующий раз прицепи брелок ярче."
                        lesha "Спасибо. С меня долг."
                        $ empathy += 1
                        $ money += 5

                    "Спрятать ключи и соврать, что ничего не нашел.":
                        p "Пусто. Может, у киоска потерял."
                        lesha "Понял..."
                        narr "Через минуту из темной арки выходят Лёша и его друг Костя."
                        narr "Рядом появляется Санек и смотрит на тебя с презрением."
                        call show_right(["gopnik", "sanek"], ["default", "idle"]) from _call_show_right_6
                        gop "Непорядочно, Пашка. Тебе помогали — а ты человека на морозе кинул."
                        narr "Костя выхватывает у тебя спрятанные ключи и сильно толкает в плечо."
                        call stress_up(2) from _call_stress_up_4
                        if money > 0:
                            $ fine = min(money, 12)
                            $ money -= fine
                            gop "И [fine] рублей оставь на извинения."
                        call hide_right from _call_hide_right_5

            "Сказать, что спешишь домой.":
                p "Извини, не могу. Сам еле стою."
                lesha "Понял..."
    else:
        p "Без фонаря тут ничего не найти."
        lesha "Ладно, попробую у ЖЭСа дежурного разбудить."

    call hide_right from _call_hide_right_6
    return

label day2_hard_money_quest:
    scene expression day1_image("/streets/street_id_1")
    with dissolve

    call show_right(["broker", "roma", "temshik"], ["default", "idle"]) from _call_show_right_7
    broker "Пашок, есть работа на полчаса. Заплачу 180 рублей."
    p "За что такие деньги?"
    broker "Нужно донести пакет через два двора. Раз плюнуть. Тьфу."

    menu:
        "Взяться за рискованную подработку.":
            p "Говори маршрут."
            narr "Рома дает старый спортивный пакет и адрес у трамвайного кольца."
            call add_item("пакет Ромы") from _call_add_item_1
            call pass_time(30) from _call_pass_time_2

            scene expression bg_path("/courtyards/yard_id_2")
            with dissolve
            call show_right(["cop", "klimov", "police"], ["default", "idle"]) from _call_show_right_8
            cop "Документы. Что в пакете?"
            menu:
                "Ответить спокойно и не дергаться.":
                    p "Спецовка и инструменты после смены."
                    cop "Открывай."
                    narr "Внутри наверху действительно лежит роба, а ниже что-то тяжелое в ткани."
                    menu:
                        "Открыть пакет и рискнуть.":
                            narr "Климов видит только грязную спецовку и машет рукой — ему лень копаться глубже."
                            p "Я пойду?"
                            cop "Иди."
                            $ toughness += 1

                        "Резко уйти в переулок.":
                            narr "Ты срываешься с места, но нога скользит на льду."
                            cop "Стоять!"
                            menu:
                                "Побежать по левой стороне двора.":
                                    narr "Слева тупик между гаражами. Через несколько секунд тебя прижимают к стене."
                                    narr "Пакет отбирают. Рома позже за это не простит."
                                    call remove_item("пакет Ромы") from _call_remove_item
                                    $ day2_lost_roma_package = True
                                    call stress_up(3) from _call_stress_up_5
                                    $ toughness -= 1
                                    call hide_right from _call_hide_right_7
                                    return

                                "Побежать по правой стороне и сбросить пакет.":
                                    narr "Справа проход к арке. Ты швыряешь пакет в мусорный короб и ныряешь во двор-колодец."
                                    narr "Климов теряет тебя в проходных подъездах. Рома это не простит, но до участка дело не доходит."
                                    call remove_item("пакет Ромы") from _call_remove_item_1
                                    $ day2_lost_roma_package = True
                                    call stress_up(2) from _call_stress_up_6
                                    call hide_right from _call_hide_right_8
                                    return

                "Попробовать пойти дальше.":
                    p "Мне домой надо, а не в допросную."
                    cop "Теперь точно в допросную."
                    narr "Тебя держат у стены почти сорок минут, потом отпускают без пакета."
                    narr "Про пакет все уже и забыли. Им нужно было что-то от меня узнать."
                    narr "Но я так и не понял. Может спутали с кем."
                    call pass_time(40) from _call_pass_time_3
                    call remove_item("пакет Ромы") from _call_remove_item_2
                    $ day2_lost_roma_package = True
                    call stress_up(2) from _call_stress_up_7
                    call hide_right from _call_hide_right_9
                    return

            call hide_right from _call_hide_right_10
            scene expression bg_path("/courtyards/yard_id_5")
            with dissolve
            call play_horror_stinger("anomaly", 3.0) from _call_play_horror_stinger_1
            call show_right(["thin", "anomaly_tall"], ["default", "idle"]) from _call_show_right_9
            narr "В проходе стоит слишком высокий и болезненно худой человек."
            thin "Пакет не тебе."
            thin "Почему ты такой низкий и толстый?"
            narr "Пока он выговаривает слова, его плечи будто стягивает вверх: он становится еще выше и еще тоньше."
            narr "Мне не по себе."
            menu:
                "Пройти мимо, не поднимая глаз.":
                    p "Я никого не видел."
                    narr "Фигура отходит в тень, как будто складывается пополам."
                    $ stress += 1

                "Спросить, кто он.":
                    p "Кто ты?"
                    thin "..."
                    thin "Тот, кто дддойдет быстрее тттебббяя."
                    narr "Он исчезает за углом раньше, чем ты моргнул."
                    $ stress += 2

            call hide_right from _call_hide_right_11
            call restore_main_ambience from _call_restore_main_ambience_1

            scene expression day1_image("/abandoned/abandoned_id_1")
            with dissolve
            call show_right(["broker", "roma", "temshik"], ["default", "idle"]) from _call_show_right_10
            broker "Дошел. Хорошо."
            call remove_item("пакет Ромы") from _call_remove_item_3
            $ money += 180
            $ day2_easy_money_done = True
            broker "Запомни: работай со мной и поднимешь."
            p "Спасибо."

            menu:
                "Разговорить Рому про его 'историю успеха'.":
                    p "А ты сам как поднялся? Не с пакетов же начал."
                    $ roma_story = renpy.random.randint(1, 3)
                    if roma_story == 1:
                        broker "Я в девяносто втором торговал кассетами у Комаровки."
                        broker "Потом понял: кто владеет дефицитом, тот и пишет правила."
                        broker "За год с кассет перешел на технику и купил свою первую машину."
                    elif roma_story == 2:
                        broker "Меня однажды выгнали с рынка за долги."
                        broker "Я занял последние деньги, привез польские джинсы и продал за ночь втрое дороже."
                        broker "С тех пор запомнил: риск платит тем, кто не моргает."
                    else:
                        broker "Когда все рвались в челноки, я возил не вещи, а информацию."
                        broker "Кому когда закрывают точку, у кого завтра проверка, кто с кем делит склад."
                        broker "За правильный слух платят больше, чем за полный баул товара."
                    p "Угу..."
                    narr "Я ему не верю. Слишком гладко стелит."

                "Поскорее уйти, не продолжая разговор.":
                    p "Понял. Мне пора."

            call hide_right from _call_hide_right_12

        "Отказаться от сомнительной схемы.":
            p "Нет. Я до дома дойти не могу спокойно, какие пакеты."
            broker "Как знаешь. Бедность — это тоже выбор."
            $ toughness -= 1
            call hide_right from _call_hide_right_13

    return

label day2_finish:
    scene expression day1_image("/entrances/entrance_id_1")
    with dissolve

    if day2_easy_money_done:
        narr "В кармане непривычно тяжело от купюр, а на душе еще тяжелее."
        p "Сколько лет жизни я уже обменял на деньги, которых все равно не хватает?"
        p "И почему я почти не помню, что было в цехе между сиренами начала и конца смены?"
    else:
        narr "Паша поднимается к подъезду медленно, считая ступени как прожитые годы."
        p "Тридцать лет, а ощущение, будто половину уже проехал мимо своей остановки."
        p "Иногда после работы в голове туман, словно меня на день выключали из собственной жизни."

    call stop_day_clock from _call_stop_day_clock_1
    return
