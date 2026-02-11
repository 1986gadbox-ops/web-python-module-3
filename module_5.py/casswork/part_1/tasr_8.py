# ЗАДАЧА: Анализ чатов пользователей

# Даны сообщения в чате. Каждое сообщение представлено словарём
# со следующими ключами:
# - "user"      : имя пользователя (строка)
# - "text"      : текст сообщения (строка)
# - "timestamp" : время сообщения (целое число, возрастает не строго)

# Пример входных данных:
# messages = [
#     {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
#     {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
#     {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
#     {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
#     {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
#     {"user": "Боб",   "text": "пока",                  "timestamp": 20},
# ]

# НЕОБХОДИМО РЕАЛИЗОВАТЬ:

# 1. Посчитать количество сообщений каждого пользователя.
#    Результат сохранить в словарь вида:
#    {
#        "Алиса": 3,
#        "Боб": 2
#    }

# 2. Для каждого пользователя:
#    2.1 Найти множество уникальных слов, которые он использовал
#        (слова разделяются методом split()).
#    2.2 Найти самое частое слово пользователя.
#        Если самых частых слов несколько — можно выбрать любое.

# 3. Найти пользователя с самым большим словарным запасом,
#    где словарный запас — это количество уникальных слов,
#    использованных пользователем.

# 4. Найти множество слов, которые использовали ВСЕ пользователи
#    (пересечение множеств слов пользователей).

# 5. Для каждого пользователя определить максимальный перерыв
#    между его сообщениями:
#    - перерыв = разница между timestamp текущего и предыдущего сообщения
#    - найти пользователя с самым большим таким перерывом
# """





messages = [
    {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
    {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
    {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб",   "text": "пока",                  "timestamp": 20},
]


user_time = {}
user_words = {}
messages_count = {}
for message in messages:
    user = message["user"]
    words = message["text"].split()
    timestamp = message["timestamp"]
    messages_count[user] = messages_count.get(user, 0) + 1
    
    if user not in user_words:
        user_words[user] = set()
    user_words[user].update(message["text"].split())


most_freg_words = {}
for user_name in user_words:
    freg = {}
    for message in messages:
        if user_name == message["user"]:
            for word in message["text"].split():
                freg[word] = freg.get(word, 0) + 1

    max_word = None
    max_count = 0

    for word,count in freg.items():
        if count > max_count:
            max_word = word
            max_count = count
    most_freg_words[user_name] = max_word


for user_name in user_time:
    user_time

print(messages_count)
print(user_words)
print(max_word)
print(most_freg_words)
    



