"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib
import random

url_dict = {
    '804286e2186e918cf9d0c78750a6e1a5af4b2782053ca52148b76d8cc96bbf8d647c39207a53af0baf7c4945088be987af3387c37735c0784d7b301ee49e1b4a': 'https://geekbrains.ru/'}


def hash_url(url, dict_add):
    """Создаём хеш страницы добавляем "соль" и вносим в словарь"""
    hash_url_address = hashlib.sha256((url).encode()).hexdigest() + hashlib.sha256(
        (str(random.randint(0, 1000000)).encode())).hexdigest()
    dict_add.setdefault(hash_url_address, url)
    return f'{dict_add.get(hash_url_address)} {hash_url_address}'


def check_url(dict_address):
    """Проверяем наличие хеша страницы в словаре по ключу при помощи среза,
     если страницы нет инициализируем добавление в словарь"""
    url = input("Введите адрес для проверки: ")
    if hashlib.sha256((url).encode()).hexdigest() in [i[:64] for i in url_dict.keys()]:
        return 'Данная страница уже хэширована'
    else:
        return hash_url(url, dict_address)

check_url (url_dict )
"""
Для проверки
https://www.google.com/ Занесёт страницу в хэш-словарь
https://geekbrains.ru/ Выдаст информацию о наличии в хэш-словаре
"""