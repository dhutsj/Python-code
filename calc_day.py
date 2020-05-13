import datetime


def calc_day():
    year = input('Please input year: ')
    month = input('Please input month: ')
    day = input('Please input day: ')
    d1 = datetime.datetime(year=int(year), month=int(month), day=int(day))
    d2 = datetime.datetime(year=int(year), month=1, day=1)
    day = d1 - d2
    return day.days + 1


print calc_day()
