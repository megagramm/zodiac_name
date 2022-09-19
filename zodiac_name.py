import datetime


def main():
    year = int(input('Введи год своего рождения: '))
    month = int(input('Введи месяц своего рождения: '))
    day = int(input('Введи день своего рождения: '))

    print(get_zodiac_name(year, month, day))


def get_zodiac_name(year, month, day):
    # Возвращает название знака зодиака по дате

    birthday = datetime.date(year, month, day)  # Создает объект даты. Не позволит ввести несуществующую дату
    birthday_day_of_year = int(birthday.strftime('%j'))  # Покажет порядковый номер ДР в году
    days_in_year = int(datetime.date(year, 12, 31).strftime('%j'))  # Сколько дней в году?
    leap_year = bool(days_in_year % 365)  # високосный год, если високосный будет прибавляться +1 день к сравнениям

    if birthday_day_of_year < 21:
        zodiak_name = 'Козерог'
    elif birthday_day_of_year < 51:
        zodiak_name = 'Водолей'
    elif birthday_day_of_year < 80 + leap_year:
        zodiak_name = 'Рыбы'
    elif birthday_day_of_year < 111 + leap_year:
        zodiak_name = 'Овен'
    elif birthday_day_of_year < 141 + leap_year:
        zodiak_name = 'Телец'
    elif birthday_day_of_year < 173 + leap_year:
        zodiak_name = 'Близнецы'
    elif birthday_day_of_year < 204 + leap_year:
        zodiak_name = 'Рак'
    elif birthday_day_of_year < 236 + leap_year:
        zodiak_name = 'Лев'
    elif birthday_day_of_year < 267 + leap_year:
        zodiak_name = 'Дева'
    elif birthday_day_of_year < 297 + leap_year:
        zodiak_name = 'Весы'
    elif birthday_day_of_year < 327 + leap_year:
        zodiak_name = 'Скорпион'
    elif birthday_day_of_year < 356 + leap_year:
        zodiak_name = 'Стрелец'
    else:
        zodiak_name = 'Козерог'

    return zodiak_name


if __name__ == '__main__':
    main()
