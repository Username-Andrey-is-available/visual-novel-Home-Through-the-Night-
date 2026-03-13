# Core state and helper labels

default day = 1
default money = 10
default stress = 0
default inventory = []
default empathy = 0
default toughness = 0

default inventory_capacity = 4

default game_minutes = 20 * 60 + 30
default clock_running = False
default deadline_failed = False
default darkness_alpha = 0.0

default day1_paid_gopniks = False
default day1_helped_oldwoman = False
default day1_talked_football = False
default day1_found_safe_route = False
default day2_lost_keys_resolved = False
default day2_easy_money_done = False
default day2_lost_roma_package = False
default day1_agreed_beer = False
default shift_bonus_days = []

default day3_student_date_agreed = False
default day3_met_dvornik = False
default day3_face_man_hint = False
default day3_librarian_factory_phrase_heard = False
default day3_dvornik_money = 10
default day3_dvornik_win_streak = 0
default day3_dvornik_refused_rematch = False

default day4_night_checked_door = False
default day4_peephole_event_seen = False
default day4_faceless_phrase_heard = False
default day4_time_frozen = False
default day4_frozen_minutes = 0
default day4_split_personality_revealed = False

default day3_abandoned_target = ""

default day5_understood_death_link = False
default day5_police_suspicion = False
default day5_waited_for_boy = False
default day5_quests_done = 0
default day5_arrested = False
default day5_disposed_gun = False
default day5_oldwoman_hint = False

default day6_lina_met = False
default day6_lina_alive = False
default day6_disposed_evidence = False
default day6_used_needles = False
default day6_used_spokes = False

default lina_die = False

default total_quest_flags = [
    "day1_paid_gopniks",
    "day1_helped_oldwoman",
    "day1_talked_football",
    "day1_found_safe_route",
    "day2_lost_keys_resolved",
    "day2_easy_money_done",
    "day3_student_date_agreed",
    "day3_met_dvornik",
    "day3_librarian_factory_phrase_heard",
    "day4_peephole_event_seen",
    "day4_faceless_phrase_heard",
    "day4_split_personality_revealed",
    "day5_understood_death_link",
    "day5_waited_for_boy",
]


init python:
    import os
    import re

    def pick_existing(candidates):
        for c in candidates:
            if renpy.loadable(c):
                return c
        return None

    def _normalize(s):
        return re.sub(r"[^a-z0-9]+", "", s.lower())

    def _media_files(prefixes=("images/", "image/"), exts=(".png", ".jpg", ".jpeg", ".webp")):
        files = renpy.list_files()
        out = []
        for f in files:
            low = f.lower()
            if any(low.startswith(p) for p in prefixes) and low.endswith(exts):
                out.append(f)
        return out

    def _audio_files(prefixes=("audio/",), exts=(".ogg", ".mp3", ".wav")):
        files = renpy.list_files()
        out = []
        for f in files:
            low = f.lower()
            if any(low.startswith(p) for p in prefixes) and low.endswith(exts):
                out.append(f)
        return out

    def bg_path(name):
        exts = ("png", "jpg", "jpeg", "webp")
        raw = str(name)
        clean = raw.lstrip("/")
        variants = [clean, clean.lower(), clean.upper()]
        candidates = []
        for v in variants:
            for ext in exts:
                candidates.extend([
                    f"images/bg/{v}.{ext}",
                    f"images/backgrounds/{v}.{ext}",
                    f"images/{v}.{ext}",
                    f"image/bg/{v}.{ext}",
                    f"image/backgrounds/{v}.{ext}",
                    f"image/{v}.{ext}",
                    f"{v}.{ext}",
                ])
        found = pick_existing(candidates)
        return found if found else Solid("#0a0a0a")

    def day1_image(keywords, fallback="#0a0a0a"):
        if isinstance(keywords, str):
            keywords = [keywords]
        files = _media_files()
        norm_keys = [_normalize(k) for k in keywords]

        # 1) Ищем, чтобы все ключи встретились в пути.
        for f in files:
            n = _normalize(f)
            if all(k in n for k in norm_keys):
                return f

        # 2) Ищем по любому ключу.
        for f in files:
            n = _normalize(f)
            if any(k in n for k in norm_keys):
                return f

        return Solid(fallback)

    def sprite_path(char_names, moods=("default", "idle")):
        if isinstance(char_names, str):
            char_names = [char_names]
        if isinstance(moods, str):
            moods = [moods]

        exts = ("png", "webp", "jpg", "jpeg")
        candidates = []
        for name in char_names:
            for mood in moods:
                for ext in exts:
                    candidates.extend([
                        f"images/characters/{name}/{name}_{mood}.{ext}",
                        f"images/characters/{name}_{mood}.{ext}",
                        f"images/characters/{name}.{ext}",
                        f"images/sprites/{name}/{name}_{mood}.{ext}",
                        f"images/sprites/{name}_{mood}.{ext}",
                        f"images/sprites/{name}.{ext}",
                        f"images/{name}/{name}_{mood}.{ext}",
                        f"images/{name}_{mood}.{ext}",
                        f"images/{name}.{ext}",
                        f"image/characters/{name}/{name}_{mood}.{ext}",
                        f"image/characters/{name}_{mood}.{ext}",
                        f"image/characters/{name}.{ext}",
                        f"{name}_{mood}.{ext}",
                        f"{name}.{ext}",
                    ])

        found = pick_existing(candidates)
        if found:
            return found

        # fallback: скан по ключу имени
        files = _media_files()
        for name in char_names:
            nk = _normalize(name)
            for f in files:
                if nk in _normalize(f):
                    return f

        return None

    def audio_track(stems):
        if isinstance(stems, str):
            stems = [stems]

        exts = ("ogg", "mp3", "wav")
        candidates = []
        for stem in stems:
            for ext in exts:
                candidates.extend([
                    f"audio/{stem}.{ext}",
                    f"{stem}.{ext}",
                ])

        found = pick_existing(candidates)
        if found:
            return found

        # fallback: нормализованный поиск по существующим audio/*
        files = _audio_files()
        norm_stems = [_normalize(s) for s in stems]
        for f in files:
            nf = _normalize(f)
            if any(ns in nf or nf in ns for ns in norm_stems):
                return f
        return None


    def format_game_time(total_minutes):
        h = (total_minutes // 60) % 24
        m = total_minutes % 60
        return "{:02d}:{:02d}".format(h, m)

    def sanitize_return_stack():
        """Убирает устаревшие точки return из старых сохранений после изменений сценария."""
        ctx = renpy.game.context()
        removed = 0

        while getattr(ctx, "return_stack", None):
            try:
                ctx.lookup_return(pop=False)
                break
            except Exception:
                ctx.return_stack.pop()
                removed += 1

        return removed

    def delete_all_saves():
        """Полное удаление файлов сохранений текущей игры."""
        removed = 0

        # Удаляем слоты через API Ren'Py.
        for save_data in renpy.list_saved_games(fast=True):
            try:
                renpy.unlink_save(save_data[0])
                removed += 1
            except Exception:
                pass

        # Не удаляем произвольные служебные файлы из savedir (например persistent),
        # чтобы не ломать текущую сессию и не сбрасывать игру в "Новая игра".

        renpy.notify("Сохранения удалены")
        return None


    def day_with_weekday(day_num):
        names = {
            1: "Понедельник",
            2: "Вторник",
            3: "Среда",
            4: "Четверг",
            5: "Пятница",
            6: "Суббота",
            7: "Воскресенье",
        }
        return "День {} — {}".format(day_num, names.get(day_num, "Неизвестно"))

    def completed_quest_ratio():
        flags = list(getattr(store, "total_quest_flags", []))
        if not flags:
            return 0.0

        done = 0
        for flag in flags:
            if bool(getattr(store, flag, False)):
                done += 1
        return float(done) / float(len(flags))

    def update_game_clock():
        if not store.clock_running:
            return

        store.game_minutes += 1

        # После 22:00 фон темнеет на 15% каждые 5 игровых минут.
        over = max(0, store.game_minutes - (22 * 60))
        steps = over // 5
        store.darkness_alpha = min(0.90, steps * 0.15)

        # В 22:30 срабатывает провал по времени.
        if store.game_minutes >= (22 * 60 + 30):
            store.deadline_failed = True
            store.clock_running = False

    def inventory_icon_path(item_name):
        n = _normalize(item_name)
        files = _media_files()
        for f in files:
            low = f.lower()
            if "/items/" in low and n in _normalize(f):
                return f
        return None


label after_load:
    $ removed_returns = sanitize_return_stack()
    if removed_returns > 0:
        $ renpy.notify("Старое сохранение обновлено после изменений сценария")
    return


label init_day_clock(start_hour=20, start_minute=30):
    $ game_minutes = start_hour * 60 + start_minute
    $ darkness_alpha = 0.0
    $ deadline_failed = False
    $ clock_running = True
    return


label apply_shift_bonus:
    if day not in shift_bonus_days:
        $ shift_income = renpy.random.randint(1, 20)
        $ money += shift_income
        $ shift_bonus_days.append(day)
        narr "После смены выдали [shift_income] ₽ переработки."
        if shift_income <= 5:
            p "М-да... за такую 'премию' даже злиться лень."
        elif shift_income >= 15:
            p "Ого. Сегодня хотя бы не зря глотал заводскую пыль."
        else:
            p "Нормально. На пару дней станет полегче."
    return

label stop_day_clock:
    $ clock_running = False
    return

label ensure_main_ambience:
    $ main_track = audio_track("walk")
    if main_track:
        play music main_track fadein 1.0 loop
    return

label play_horror_stinger(next_theme="anomaly", duration=3.0):
    $ stinger_track = audio_track(["screamer", "horror-stinger", "scary-hit"])
    if stinger_track:
        play sound stinger_track

    $ renpy.pause(duration, hard=True)

    if next_theme == "anomaly":
        call switch_to_anomaly_ambience from _call_switch_to_anomaly_ambience_1
    elif next_theme:
        call play_safe_dialog_music(next_theme) from _call_play_safe_dialog_music_3
    return

label switch_to_anomaly_ambience:
    $ anomaly_track = audio_track(["horror-background_id_1", "dark-horror-background-id1", "dark-horror-background_id_1"])
    if anomaly_track:
        play music anomaly_track fadeout 0.5 fadein 0.5 loop
    return

label restore_main_ambience:
    call ensure_main_ambience from _call_ensure_main_ambience_7
    return

label play_safe_dialog_music(theme_name=""):
    $ stem = str(theme_name).lower().strip()
    if stem:
        $ safe_track = audio_track([f"{stem}_theme", f"{stem}-theme", f"theme_{stem}", stem])
        if safe_track:
            play music safe_track fadeout 0.5 fadein 0.5 loop
    return

label show_right(char_names, moods=("default", "idle")):
    $ sp = sprite_path(char_names, moods)
    if sp:
        show expression sp as side_character at right
    return

label hide_right:
    hide side_character
    return

label add_item(item_name):
    if item_name not in inventory:
        $ inventory.append(item_name)
        narr "Получен предмет: [item_name]."
    return

label remove_item(item_name):
    if item_name in inventory:
        $ inventory.remove(item_name)
        narr "Предмет убран: [item_name]."
    return

label pass_time(minutes=0):
    if clock_running and minutes > 0:
        $ game_minutes += minutes
    return

label spend_money(amount):
    if money >= amount:
        $ money -= amount
        return True
    return False

label stress_up(amount=1):
    $ stress += amount
    if stress >= 9 and toughness < 4:
        jump ending_burnout
    return
