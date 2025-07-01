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
    "apple", "baby", "ball", "banana", "bank", "bath", "bear", "bed", "bee", "bell",
    "bird", "book", "boot", "box", "boy", "bread", "brother", "bus", "cake", "car",
    "cat", "chair", "cheese", "child", "chicken", "clock", "cloud", "coat", "corn", "cow",
    "cup", "dad", "dance", "day", "dog", "door", "duck", "ear", "egg", "eye",
    "face", "farm", "father", "feet", "fish", "floor", "flower", "fly", "food", "foot",
    "fork", "friend", "frog", "game", "garden", "girl", "goat", "grape", "grass", "ground",
    "hair", "hand", "hat", "head", "heart", "hill", "home", "horse", "house", "ice",
    "island", "jam", "juice", "key", "king", "knee", "knife", "lady", "lamp", "leaf",
    "leg", "lemon", "letter", "line", "lion", "lip", "lock", "man", "map", "milk",
    "money", "monkey", "moon", "mother", "mouse", "mouth", "name", "nest", "night", "nose",
    "nut", "orange", "oven", "page", "paint", "paper", "park", "party", "pen", "pencil",
    "pet", "pig", "plane", "plant", "plate", "play", "plum", "pocket", "pot", "queen",
    "rabbit", "rain", "rat", "rice", "ring", "river", "road", "rock", "roof", "room",
    "root", "rose", "salt", "sand", "school", "seed", "sheep", "shirt", "shoe", "shop",
    "sister", "sky", "snake", "snow", "sock", "son", "song", "spoon", "star", "stick",
    "stone", "street", "sun", "table", "tail", "teacher", "team", "teeth", "tent", "test",
    "tie", "time", "toe", "tomato", "tool", "tooth", "toy", "train", "tree", "truck",
    "uncle", "wall", "water", "way", "wheel", "window", "wing", "woman", "wood", "word",
    "work", "worm", "yard", "zebra", "zero", "bag", "bat", "cap", "cupboard", "desk",
    "fan", "flag", "glove", "lamp", "mat", "pan", "pen", "pet", "rope", "rug",
    "sack", "soap", "tap", "van", "vest", "web", "well", "wish", "yarn", "zip",
    "actor", "adult", "age", "air", "anger", "animal", "answer", "area", "arm", "army",
    "art", "attack", "aunt", "baby", "back", "bag", "ball", "band", "bank", "base",
    "basket", "bath", "battle", "beach", "bear", "beat", "beauty", "bed", "bee", "bell",
    "belt", "berry", "bird", "birth", "bite", "blade", "blood", "board", "boat", "body",
    "bone", "book", "boot", "border", "bottle", "bottom", "box", "boy", "brain", "branch",
    "brass", "bread", "break", "brick", "bridge", "brother", "brush", "bubble", "bucket", "building",
    "bulb", "bun", "burn", "burst", "bus", "bush", "butter", "button", "cake", "camera",
    "camp", "can", "candle", "cap", "car", "card", "care", "carriage", "cart", "cat",
    "cause", "chain", "chalk", "chance", "change", "cheese", "cherry", "chest", "chicken", "child",
    "chin", "church", "circle", "city", "class", "clock", "cloud", "coat", "collar", "comb",
    "committee", "company", "comparison", "competition", "condition", "connection", "control", "cook", "copper", "copy",
    "cord", "cork", "corn", "cough", "country", "cover", "cow", "crack", "credit", "crime",
    "crush", "cry", "cup", "cupboard", "current", "curtain", "curve", "cushion", "damage", "danger",
    "daughter", "day", "death", "debt", "decision", "degree", "design", "desire", "desk", "detail",
    "development", "digestion", "direction", "discovery", "discussion", "disease", "disgust", "distance", "distribution", "division",
    "dog", "door", "doubt", "drain", "drawer", "dress", "drink", "driving", "drop", "dust",
    "ear", "earth", "edge", "education", "effect", "egg", "elastic", "end", "engine", "error",
    "event", "example", "exchange", "existence", "expansion", "experience", "expert", "eye", "face", "fact",
    "fall", "family", "farm", "father", "fear", "feather", "feeling", "female", "fertile", "fiction",
    "field", "fight", "finger", "fire", "fish", "flag", "flame", "flat", "flight", "floor",
    "flower", "fly", "fold", "food", "foot", "force", "fork", "form", "fowl", "frame",
    "friend", "frog", "fruit", "fuel", "full", "future", "garden", "girl", "glass", "glove",
    "goat", "gold", "good", "government", "grain", "grass", "grip", "group", "growth", "guide",
    "gun", "hair", "hammer", "hand", "harbor", "harmony", "hat", "hate", "hearing", "heart",
    "heat", "help", "history", "hole", "holiday", "home", "hook", "hope", "horn", "horse",
    "hospital", "hour", "house", "humor", "ice", "idea", "impulse", "income", "increase", "industry",
    "ink", "insect", "instrument", "insurance", "interest", "invention", "iron", "island", "jelly", "jewel",
    "join", "journey", "judge", "jump", "kick", "kiss", "knee", "knife", "knot", "knowledge",
    "land", "language", "laugh", "law", "lead", "leaf", "learning", "leather", "leg", "letter",
    "level", "library", "lift", "light", "limit", "line", "linen", "lip", "liquid", "list",
    "lock", "look", "loss", "love", "machine", "magic", "man", "manager", "map", "market",
    "mass", "match", "meal", "measure", "meat", "meeting", "memory", "metal", "middle", "milk",
    "mind", "mine", "minute", "mist", "money", "monkey", "month", "moon", "morning", "mother",
    "motion", "mountain", "mouth", "move", "muscle", "music", "nail", "name", "nation", "neck",
    "needle", "nerve", "net", "news", "night", "noise", "nose", "note", "number", "nut",
    "office", "oil", "operation", "opinion", "orange", "order", "organization", "ornament", "oven", "owner",
    "page", "pain", "paint", "paper", "parcel", "part", "partner", "party", "paste", "payment",
    "peace", "pen", "pencil", "person", "pet", "picture", "pig", "pin", "pipe", "place",
    "plane", "plant", "plate", "play", "pleasure", "plough", "pocket", "point", "poison", "polish",
    "porter", "position", "pot", "potato", "powder", "power", "price", "print", "prison", "process",
    "produce", "profit", "property", "prose", "protest", "pull", "pump", "punishment", "purpose", "push",
    "queen", "question", "quiet", "rabbit", "rain", "range", "rat", "ray", "reaction", "reading",
    "reason", "receipt", "record", "regret", "relation", "religion", "representative", "request", "respect", "rest",
    "reward", "rhythm", "rice", "ring", "river", "road", "rod", "roll", "roof", "room",
    "root", "rose", "rule", "run", "sad", "salt", "sand", "scale", "school", "science",
    "scissors", "screw", "sea", "seat", "secret", "seed", "selection", "self", "sense", "servant",
    "sex", "shade", "shake", "shame", "shape", "sheep", "shelf", "ship", "shirt", "shock",
    "shoe", "shop", "show", "side", "sign", "silk", "silver", "sister", "size", "skirt",
    "sky", "sleep", "slip", "slope", "smash", "smell", "smile", "smoke", "snake", "sneeze",
    "snow", "soap", "society", "sock", "son", "song", "sort", "sound", "soup", "space",
    "spade", "spark", "spoon", "spring", "square", "stage", "stamp", "star", "start", "statement",
    "station", "steam", "steel", "stem", "step", "stick", "stocking", "stomach", "stone", "stop",
    "store", "story", "street", "stretch", "string", "summer", "sun", "support", "surprise", "swim",
    "system", "table", "tail", "talk", "taste", "tax", "teaching", "tendency", "test", "theory",
    "thing", "thought", "thread", "throat", "thumb", "thunder", "ticket", "time", "tin", "toe",
    "tomato", "tongue", "tooth", "town", "trade", "train", "tray", "tree", "trick", "trouble",
    "trousers", "truck", "turn", "twist", "umbrella", "uncle", "unit", "use", "value", "verse",
    "vessel", "view", "voice", "walk", "wall", "war", "wash", "waste", "watch", "water",
    "wave", "wax", "way", "weather", "week", "weight", "wheel", "whip", "whistle", "window",
    "wine", "wing", "winter", "woman", "wood", "wool", "word", "work", "worm", "wound",
    "writing", "year", "yellow", "yoke", "zebra", "zero"
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