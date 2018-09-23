# Ближайшие бары
Программа позволяет определить самый большой и маленький бар, используя данные из файла формата json. Также самый ближайший, после того как пользователь введет свои координаты. Файл можно скачать на [портале открытых данных правительства Москвы](https://data.mos.ru/opendata/7710881420-bary).
# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и дополнительного модуля geopy, который нужен для нахождения ближайшего бара. Установить данный модуль можно, выполнив команду: ```pip install -r requirements.txt```

Запуск на Linux:

```bash

$ python bars.py <file_name>.json

# Пример:
$ python bars.py bars.json
Самый большой бар - Спорт бар «Красная машина». 
Самый маленький бар - БАР. СОКИ.
Введите долготу: 37.5992518
Введите широту: 55.7496363
Ближайший к Вам бар:  Винный кофейный бар 45



```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
