from random import choice



def ru_words():
    ru_words = [
    "автобус", "агроном", "аллея", "альбом", "аптека", "аромат", "астраханец", "аэропорт", "балкон", "барабан",
    "барьер", "бассейн", "батон", "башня", "белка", "берег", "береза", "билет", "бинокль", "блокнот",
    "больница", "борода", "ботинок", "бочка", "брат", "брусника", "букет", "бумага", "бутылка", "вагон",
    "ваза", "валенок", "валюта", "ванна", "варежка", "вафля", "вдова", "верблюд", "веревка", "вертолет",
    "весло", "ветер", "ветка", "вилка", "виноград", "вишня", "вода", "водопад", "воздух", "волейбол",
    "волк", "волна", "воробей", "ворота", "воск", "восток", "врач", "время", "всадник", "вулкан",
    "газета", "галстук", "гвоздика", "гвоздь", "гитара", "глина", "глобус", "гнездо", "голубь", "город",
    "горох", "горшок", "грабли", "градусник", "грамота", "гриб", "груша", "грузовик", "губка", "дача",
    "дворец", "девочка", "дедушка", "дежурный", "день", "дерево", "десерт", "дождь", "домино", "доска",
    "дочка", "дракон", "дрова", "дружба", "дуга", "дым", "дыня", "ежевика", "ежик", "жабра",
    "жакет", "жара", "жасмин", "железо", "желток", "жеребец", "жираф", "жук", "забор", "завод",
    "загадка", "зайка", "заяц", "зебра", "земля", "зеркало", "зима", "змея", "зонт", "игла",
    "игра", "игрушка", "идея", "изба", "изюм", "икра", "имя", "индюк", "иней", "инструмент",
    "искра", "кабачок", "кабинет", "кактус", "калитка", "камень", "каникулы", "капля", "карандаш", "карета",
    "картофель", "кастрюля", "катер", "кафе", "квадрат", "кедр", "кенгуру", "кино", "кирпич", "кит",
    "клавиатура", "клен", "книга", "кнопка", "ковер", "ковш", "коготь", "код", "козел", "коза",
    "козырек", "колесо", "колено", "колесница", "колодец", "колос", "коляска", "команда", "комар", "комета",
    "комната", "компас", "конверт", "конек", "конь", "корабль", "корзина", "коридор", "корова", "корона",
    "корпус", "коса", "космос", "кость", "кот", "котенок", "кофе", "кочан", "краб", "краска",
    "кран", "кровать", "кролик", "круг", "кружка", "крыша", "кукла", "кукуруза", "кулак", "купол",
    "курица", "куст", "кухня", "лабиринт", "лавка", "ладонь", "лампа", "лань", "лапша", "ларец",
    "ласточка", "лев", "лес", "леска", "лесник", "лестница", "лето", "лиана", "лист", "листва",
    "линия", "лиса", "листок", "лодка", "ложка", "лопата", "лось", "лук", "луна", "луч",
    "лыжи", "магазин", "майка", "мак", "макарон", "маляр", "мандарин", "марка", "маска", "масло",
    "математика", "матрас", "медаль", "медведь", "мел", "меню", "метла", "меч", "мешок", "микрофон",
    "мишка", "молния", "молоко", "молоток", "монета", "море", "морковь", "мост", "мотоцикл", "мухомор",
    "мышь", "набор", "накидка", "наковальня", "наледь", "нальчик", "наука", "небо", "неделя", "незабудка",
    "немец", "нефть", "нож", "ножницы", "нос", "носорог", "ночь", "нога", "нога", "обед",
    "облако", "обложка", "обувь", "овощ", "огонь", "огурец", "одежда", "озеро", "окно", "окунь",
    "олень", "омлет", "операция", "опушка", "орел", "орех", "осень", "осетр", "остров", "отвертка",
    "отель", "отпуск", "отражение", "отрывок", "охота", "очередь", "очки", "павлин", "пакет", "палата",
    "пальто", "папка", "папоротник", "парк", "паром", "парус", "паспорт", "пастух", "песок", "петух",
    "печенье", "пещера", "пила", "пингвин", "писатель", "письмо", "пицца", "пламя", "планета", "платок",
    "племя", "плита", "пловец", "площадь", "плот", "плюш", "погода", "подвал", "подушка", "пожар",
    "поздравление", "позвоночник", "покрывало", "поле", "полка", "полоса", "полотенце", "полюс", "помидор", "помощник",
    "попугай", "порог", "поросенок", "портфель", "поток", "почка", "праздник", "прачка", "предмет", "призрак",
    "природа", "пристань", "пробка", "провод", "программа", "промежуток", "пруд", "птица", "пудель", "пуля",
    "пыль", "пятно", "рабочий", "радость", "разговор", "раздел", "разноцветие", "район", "ракета", "рамка",
    "ракушка", "рассвет", "растение", "расческа", "ребенок", "ребро", "река", "ремень", "ресторан", "рисунок",
    "роза", "ромашка", "роща", "рубашка", "рукав", "рулет", "руль", "ручей", "ручка", "рыба",
    "рыбак", "рыжик", "рынок", "рябина", "сад", "садовник", "салат", "самолет", "сапог", "сахар",
    "свет", "свинья", "свисток", "север", "село", "семья", "сено", "сентябрь", "сердце", "сигнал",
    "сиденье", "сирень", "скворец", "скейт", "скворечник", "склад", "сковорода", "скрипка", "скула", "скунс",
    "сладость", "слово", "слон", "слушатель", "снег", "снеговик", "сова", "совет", "сок", "солдат",
    "солома", "солнце", "сосна", "сосулька", "сочинение", "спектакль", "спинка", "спичка", "спорт", "спутник",
    "стадион", "стакан", "старание", "старт", "статуя", "стебель", "стена", "степь", "стих", "стол",
    "столб", "столик", "столяр", "сторона", "сторож", "страна", "стриж", "строка", "струна", "студент",
    "стул", "сумка", "суп", "сурок", "сухарь", "сфера", "сцена", "сыр", "сырник", "сюрприз",
    "таблетка", "табун", "тайна", "такси", "талант", "танец", "танк", "тапки", "тарелка", "театр",
    "текст", "телевизор", "телега", "телефон", "температура", "теннис", "тепло", "терем", "термос", "тесто",
    "тетрадь", "тигр", "ткань", "товарищ", "токарь", "толпа", "томат", "тон", "тополь", "торт",
    "трава", "трактор", "трамвай", "трансформатор", "треугольник", "тропинка", "тростник", "труба", "туман", "тюльпан",
    "узор", "улица", "улитка", "умение", "униформа", "урожай", "урок", "утка", "утюг", "фартук",
    "февраль", "фен", "фермер", "фигура", "филин", "фильм", "финик", "флаг", "фломастер", "фонарь",
    "форма", "форт", "фотография", "фраза", "фрукт", "футбол", "халва", "хвост", "химия", "хитрость",
    "хлеб", "хлопок", "холод", "хомяк", "хор", "художник", "цветок", "цирк", "цитрус", "чай",
    "чайка", "час", "часы", "чашка", "черепаха", "черника", "черта", "чертеж", "чехол", "чипсы",
    "чистота", "чудо", "шапка", "шар", "шарик", "шахматы", "шашка", "швейцар", "шеврон", "школа",
    "шкура", "шляпа", "шоколад", "шорты", "шоссе", "шофер", "шпагат", "шпион", "шуба", "щавель",
    "щенок", "щука", "экзамен", "экран", "электричество", "эмаль", "энергия", "эскиз", "этаж", "этикетка",
    "юбка", "юла", "юность", "юрист", "яблоко", "ягода", "якорь", "яйцо", "якорь", "ястреб"
    ]
    


    secret_word = choice(ru_words)
    attempts = 6
    secret_word_lst = list(secret_word)
    show_word = ['_'] * len(secret_word)
    letter_lst = []
    while attempts > 0:

        letter = input("Введите букву: ").lower()

        if len(letter) != 1:
            print('Введите только одну букву!')
        elif len(letter) == 1:
            if letter not in letter_lst:
                letter_lst.append(letter)
                if letter in secret_word_lst:
                    for i in range(len(secret_word_lst)):
                        if secret_word_lst[i] == letter:
                            show_word[i] = letter
                    print(f'Правильно! Буква {letter} есть в загаданном слове')
                    print(' '.join(show_word))
                    if secret_word_lst == show_word:
                        print('Подравляю! Вы победили!')
                        exit()
        
        

                elif letter not in secret_word_lst:
                    attempts -= 1
                    if attempts <= 5: print("__")
                    if attempts <= 4: print(" | ")
                    if attempts <= 3: print(" O ")
                    if attempts <= 2: print("/|\\")
                    if attempts <= 1: print(" | ")
                    if attempts <= 0: print("/ \\")
                    print(f'Увы! Буквы {letter} нет в загаданном слове')
                    continue
            elif letter in letter_lst:
                print('Вы уже вводили эту букву')
                continue

    if attempts == 0:
        print(f'Вы проиграли')
        print(f'Правильным словом было: {secret_word}')

    



def en_words():
    en_words = [
    "anchor", "artist", "autumn", "badge", "baker", "balcony", "banana", "basket", "beacon", "beaver",
    "beetle", "breeze", "bridge", "bronze", "bubble", "bucket", "butter", "button", "cactus", "camera",
    "candle", "carpet", "castle", "celery", "cheese", "cherry", "circle", "clover", "coffee", "comet",
    "cookie", "coral", "cotton", "crayon", "cricket", "crunch", "crystal", "curtain", "dagger", "dainty",
    "dancer", "desert", "dimple", "dollar", "donkey", "dragon", "drawer", "drizzle", "duplex", "eagle",
    "echo", "ember", "engine", "enigma", "fabric", "falcon", "fiddle", "figure", "filter", "finger",
    "flavor", "flower", "forest", "fortune", "fossil", "freight", "fridge", "frosty", "gadget", "garden",
    "garlic", "gazebo", "genius", "ginger", "giraffe", "glider", "goblet", "gopher", "gossip", "gravel",
    "groove", "guitar", "hammer", "hazard", "helmet", "hermit", "hinge", "hobbit", "hockey", "hollow",
    "honey", "hornet", "hurdle", "hybrid", "icicle", "ignite", "impact", "infant", "island", "ivy",
    "jacket", "jargon", "jersey", "jigsaw", "jingle", "jockey", "jungle", "karate", "kitten", "ladder",
    "lagoon", "lantern", "laptop", "larder", "lariat", "laundry", "legacy", "legend", "lemur", "lichen",
    "lizard", "locust", "lotion", "lumber", "magnet", "mantis", "marble", "market", "marrow", "matrix",
    "meadow", "meteor", "mimic", "minnow", "mirror", "monkey", "morale", "mosaic", "muffin", "museum",
    "mystic", "nachos", "napkin", "nectar", "needle", "nickel", "nugget", "obelisk", "octave", "octopus",
    "omelet", "onion", "opal", "orange", "orchid", "outlet", "oxygen", "packet", "paddle", "palace",
    "pantry", "parade", "parrot", "pastel", "pebble", "pellet", "pepper", "pickle", "pigeon", "pillow",
    "pirate", "planet", "plasma", "plenty", "plover", "poetry", "polish", "potato", "powder", "prairie",
    "prince", "prison", "puzzle", "quartz", "quiche", "quiver", "rabbit", "radish", "raisin", "ranger",
    "rascal", "rattle", "raven", "razor", "reboot", "refuge", "relic", "remedy", "rescue", "ribbon",
    "rocket", "roster", "rubber", "rudder", "saddle", "salmon", "saucer", "scarab", "scenic", "scooter",
    "scroll", "sequin", "shadow", "shovel", "shrimp", "signal", "silver", "simple", "siren", "skater",
    "sketch", "skull", "slalom", "slayer", "slider", "sneeze", "socket", "sorbet", "sphinx", "sphere",
    "spider", "spirit", "sponge", "sprout", "squash", "squire", "stable", "staple", "starch", "stereo",
    "sting", "stitch", "stork", "stream", "stripe", "studio", "subtle", "sultan", "summer", "sunset",
    "swamp", "swoosh", "symbol", "tablet", "talent", "tamale", "temple", "throne", "ticket", "timber",
    "tomato", "tongue", "topaz", "torch", "toucan", "trench", "trifle", "trivia", "trophy", "tulip",
    "tumble", "turtle", "twig", "twirl", "unicorn", "utopia", "vacuum", "valley", "velvet", "vermin",
    "vessel", "victor", "violet", "vortex", "walnut", "warden", "warrior", "wasabi", "weasel", "widget",
    "wizard", "wobble", "wonder", "wrench", "wrinkle", "yogurt", "yonder", "zealot", "zephyr", "zipper",
    "zodiac", "zombie", "zucchini", "abroad", "accent", "admire", "affect", "agenda", "alpine", "amazed",
    "anthem", "arcade", "avenue", "baboon", "ballet", "bamboo", "beacon", "beagle", "beetle", "bistro"
    ]
    


    secret_word = choice(en_words)
    attempts = 6
    secret_word_lst = list(secret_word)
    show_word = ['_'] * len(secret_word)
    letter_lst = []
    while attempts > 0:
        letter = input("Input letter: ").lower()

        if len(letter) != 1:
            print('Input only one letter!')
        elif len(letter) == 1:
            if letter not in letter_lst:
                letter_lst.append(letter)
                if letter in secret_word_lst:
                    for i in range(len(secret_word_lst)):
                        if secret_word_lst[i] == letter:
                            show_word[i] = letter
                    print(f'Correct! Letter {letter} in list')
                    print(' '.join(show_word))
                    if secret_word_lst == show_word:
                        print('Congratulations! You won the game')
                        exit()
        
        

                elif letter not in secret_word_lst:
                    attempts -= 1
                    if attempts <= 5: print("__")
                    if attempts <= 4: print(" | ")
                    if attempts <= 3: print(" O ")
                    if attempts <= 2: print("/|\\")
                    if attempts <= 1: print(" | ")
                    if attempts <= 0: print("/ \\")
                    print(f'Letter {letter} not in word')
                    continue
            elif letter in letter_lst:
                print('You already input this letter!')
                continue
        
    if attempts == 0:
        print(f'You lost')
        print(f'Correct word was {secret_word}')

preset = input('''Choose language | Выберите язык
en for English | en для английского языка
ru for Russian | ru для русского языка
               ''')


if preset == 'en':
    en_words()
if preset == 'ru':
    ru_words()